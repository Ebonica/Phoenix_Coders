# Master README

**Phoenix_Coders - Master (Med Bot & NutriScan)**

This project combines **Med Bot** and **NutriScan** into a unified Django web application. Med Bot provides an AI-powered medical chatbot using the **Ollama Llama 3.2** model, while NutriScan uses computer vision to identify food items and display nutritional information.

## Features
- **Med Bot**: AI-driven chatbot for medical queries.
- **NutriScan**: Real-time food image recognition with nutritional info.
- User authentication with chat and scan history stored for personalized responses.

## Installation
1. **Clone the repository**:

   git clone https://github.com/Ebonica/Phoenix_Coders
   cd master

2. **Set up virtual environment**:
  
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate


3. **Install dependencies**:

   pip install -r requirements.txt


4. **Migrate the database**:

   python manage.py migrate


5. **Run the server**:

   python manage.py runserver


## Usage
1. **Med Bot**: Log in to interact with the AI chatbot for medical advice.
2. **NutriScan**: Use the camera to scan food items and get nutritional information.

## License
This project is licensed under the MIT License.
