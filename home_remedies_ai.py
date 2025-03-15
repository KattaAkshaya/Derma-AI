import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def get_home_remedies(skin_type, age, gender,user_input):
    """
    Generates home remedies for skincare using Gemini AI.
    """
    prompt = f"""
    I have {skin_type} skin, I am {age} years old, and my gender is {gender}.
    I have the following skin concern: {user_input}. 
    Suggest some **effective home remedies** using natural ingredients.it should be simple and concise
    """

    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        return response.text  # Returns AI-generated text
    except Exception as e:
        return f"Error: {e}"
