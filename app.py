import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# Configure OpenAI API
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        # Read file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
st.set_page_config(page_title="Calorie Counter App")

# App header
st.title("Calorie Counter App")
st.write("Upload an image containing food items to calculate total calories and nutritional details.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Resize the image to a smaller size
    resized_image = image.resize((300, 300))  # Adjust the dimensions as needed
    st.image(resized_image, caption="Uploaded Image.")

    # Prompt and submit button
    input_prompt = """
    You are an expert in nutritionist where you need to see the food items from the image
    and calculate the total calories, also provide the details of every food items with calories intake
    in below format:
    
    1. Item 1 - no of calories
    2. Item 2 - no of calories
    ----
    ----
    Finally, also mention if food is healthy or not and also mention the percentage split of the ratio of carbohydrates, fats, fibre, sugar, protein, and other things required in our diet
    """
    
    submit = st.button("Analyze")
    
    if submit:
        st.subheader("Analysis Results:")
        
        # Generate response
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data)
        
        # Display response
        st.write(response)
