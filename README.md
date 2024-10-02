# Phoenix_Coders

NutriScan
NutriScan is a web application that uses computer vision and machine learning to identify food items from images and provide nutritional information. It's designed to help users quickly and easily get information about the food they're eating.
Features

Real-time camera feed for food image capture
Image processing to identify food items
Nutritional information display for identified foods
Responsive design for use on various devices
Progress indicators for image upload and processing

Technologies Used

Frontend: HTML, CSS, JavaScript
Backend: Python, Django
Image Processing: Pillow (Python Imaging Library)
Machine Learning: Ollama (Local LLM for image recognition and analysis)
Asynchronous Processing: aiohttp, asyncio

Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.8 or higher
pip (Python package manager)
Node.js and npm (for managing frontend dependencies, if any)
Ollama set up and running locally (for image recognition)

Installation

Clone the repository:
Copygit clone https://github.com/yourusername/nutriscan.git
cd nutriscan

Create a virtual environment and activate it:
Copypython -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required Python packages:
Copypip install -r requirements.txt

Apply database migrations:
Copypython manage.py migrate

Create a superuser (optional):
Copypython manage.py createsuperuser


Configuration

Ensure Ollama is running locally on the default port (usually 11434).
Update the OLLAMA_URL in food_recognition/views.py if your Ollama instance is running on a different port or host.
Configure your Django SECRET_KEY and other sensitive settings in a .env file (not included in version control).

Running the Application

Start the Django development server:
Copypython manage.py runserver

Open a web browser and navigate to http://localhost:8000

Usage

Allow camera access when prompted by your browser.
Point your camera at a food item.
Click the "Capture Image" button.
Wait for the image to be processed and analyzed.
View the identified food item and its nutritional information.

Contributing
Contributions to NutriScan are welcome! Please follow these steps:

Fork the repository.
Create a new branch: git checkout -b feature-branch-name.
Make your changes and commit them: git commit -m 'Add some feature'.
Push to the original branch: git push origin feature-branch-name.
Create the pull request.

Alternatively, see the GitHub documentation on creating a pull request.
License
This project is licensed under the MIT License - see the LICENSE.md file for details.
Contact
If you want to contact me, you can reach me at your ebonica7@gmail.com
Acknowledgements

Django
Ollama
Pillow
