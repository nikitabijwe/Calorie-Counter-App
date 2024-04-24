# Calorie Counter App
The Calorie Counter App is a Streamlit application that allows users to upload an image containing food items to calculate total calories and nutritional details. The app utilizes the Google Generative AI API to analyze the image and provide nutritional information for each food item detected.

## Features
- Upload Image: Users can upload an image containing food items.
- Calculate Calories: The app calculates the total calories and provides nutritional details for each food item detected in the image.
- Display Results: The app displays the analysis results, including total calories, individual food items with their respective calorie counts, and nutritional information such as carbohydrates, fats, fiber, sugar, protein, etc.
- Expert Nutritionist Prompt: The analysis is based on an expert nutritionist prompt provided by the app, ensuring accurate and detailed nutritional analysis.
- 
## Installation
- Clone the repository:
git clone https://github.com/your-username/calorie-counter-app.git

- Navigate to the project directory:
cd calorie-counter-app

- Install dependencies:
pip install -r requirements.txt

- Set up your Google API key by creating a .env file in the project directory and adding your API key:
GOOGLE_API_KEY=your-google-api-key

- Run the Streamlit app:
streamlit run app.py

## Usage
- Launch the app by running streamlit run app.py.
- Upload an image containing food items using the file uploader.
- Click the "Analyze" button to initiate the analysis process.
- The app will display the analysis results, including total calories, individual food items with their respective calorie counts, and nutritional information.
- 
# Technologies Used
- Streamlit: For building the interactive web application.
- Google Generative AI: For analyzing images and providing nutritional details.
- Python: Programming language used for backend logic.
- PIL (Python Imaging Library): For image processing and manipulation.
- 
Credits
- This app was developed by Nikita Bijwe.
