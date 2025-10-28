import google.generativeai as genai
import os
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load the .env file
load_dotenv()

# Get API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ Gemini API key is missing. Please check your .env file.")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def get_ai_recommendations(user_input, skin_type, gender, age):
    """Generate AI-powered skincare advice based on user details."""
    try:
        # Initialize the Gemini model
        model = genai.GenerativeModel("models/gemini-2.0-flash")  

        # Format the input as a single string (prompt)
        prompt = f"Provide skincare advice for a {age}-year-old {gender} with {skin_type} skin type. User query: {user_input}"

        # Get AI-generated recommendations
        response = model.generate_content(prompt)

        # Return the text response
        return response.text if response and hasattr(response, 'text') else "No response from AI."
    
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    user_input = "What are some skincare tips for dry skin?"
    skin_type = "dry"
    gender = "female"
    age = 25
    print(get_ai_recommendations(user_input, skin_type, gender, age))

