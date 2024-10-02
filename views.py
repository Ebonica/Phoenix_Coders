# food_recognition/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
import base64
import io
from PIL import Image
import aiohttp
import asyncio
import hashlib
import logging
import json

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'food_recognition/index.html')

def optimize_image(image_data, max_size=800):
    try:
        image = Image.open(io.BytesIO(base64.b64decode(image_data.split(',')[1])))
        image.thumbnail((max_size, max_size))
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG", quality=85, optimize=True)
        return base64.b64encode(buffered.getvalue()).decode('utf-8')
    except Exception as e:
        logger.error(f"Error optimizing image: {str(e)}")
        return None

@csrf_exempt
async def process_image(request):
    if request.method == 'POST':
        try:
            image_data = request.POST.get('image')
            optimized_image = optimize_image(image_data)
            if not optimized_image:
                return JsonResponse({'error': 'Failed to process image'})
            
            cache_key = hashlib.md5(optimized_image.encode()).hexdigest()
            cached_result = cache.get(cache_key)
            if cached_result:
                return JsonResponse(cached_result)
            
            prompt = "What food item is in this image? List its main nutrients."
            ollama_url = "http://localhost:11434/api/generate"
            payload = {
                "model": "llava",
                "prompt": prompt,
                "images": [optimized_image]
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(ollama_url, json=payload, timeout=30) as response:
                    if response.status == 200:
                        response_text = await response.text()
                        response_lines = response_text.strip().split('\n')
                        full_response = ''
                        for line in response_lines:
                            try:
                                json_response = json.loads(line)
                                full_response += json_response.get('response', '')
                            except json.JSONDecodeError:
                                logger.error(f"Failed to parse JSON: {line}")
                        
                        lines = full_response.split('\n')
                        food_item = lines[0] if lines else "Unknown"
                        nutrients = '\n'.join(lines[1:]) if len(lines) > 1 else "Nutrient information not available"
                        
                        result = {
                            'food_item': food_item,
                            'nutrients': nutrients
                        }
                        
                        cache.set(cache_key, result, timeout=3600)
                        return JsonResponse(result)
                    else:
                        logger.error(f"Ollama API error: {await response.text()}")
                        return JsonResponse({'error': 'Failed to process image with Ollama'})
        except asyncio.TimeoutError:
            logger.error("Ollama API timeout")
            return JsonResponse({'error': 'Ollama API timeout'})
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return JsonResponse({'error': 'An unexpected error occurred'})

    return JsonResponse({'error': 'Invalid request method'})