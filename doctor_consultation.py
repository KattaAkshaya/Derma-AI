import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Validate API Key
if not GEMINI_API_KEY:
    raise ValueError("❌ Error: GEMINI_API_KEY not found. Check your .env file.")

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

def suggest_doctor(skin_type=None, user_input=None, age=None):
    """Suggests doctor consultation based on Skin Type, Skin Concerns, or Age."""
    
    if not skin_type and not age and not user_input:
        return "⚠️ Please enter at least one detail for consultation.", None

    high_risk_conditions = {"severe acne", "psoriasis", "rosacea", "eczema", "skin infection"}
    needs_doctor = False

    # Validate age
    if isinstance(age, str) and age.strip().isdigit():
        age = int(age.strip())
        
    # If skin type is normal & no concerns, no doctor needed
    if skin_type and skin_type.lower() == "normal" and not user_input:
        return "✅ No urgent doctor consultation needed. Follow a skincare routine.", None  

    # Check user-reported conditions
    if user_input:
        user_issues = {issue.strip().lower() for issue in user_input.split(",")}
        if high_risk_conditions.intersection(user_issues):  
            needs_doctor = True

    if needs_doctor:
        doctor_needed = "⚠️ You may need to consult a dermatologist."
        detailed_advice = get_doctor_recommendation(skin_type, user_input, age)
        return doctor_needed, detailed_advice

    return "✅ No urgent doctor consultation needed. Follow a skincare routine.", None  

def get_doctor_recommendation(skin_type, skin_concerns, age):
    """Uses Gemini AI to generate personalized doctor consultation advice."""
    try:
        prompt = f"""
        I have {skin_type or "unknown"} skin, my age is {age or "unknown"}, and my skin concerns are {skin_concerns or "not specified"}. 
        
        **Instructions for AI:**
        - Provide only **medical advice** related to dermatology.
        - Exclude general skincare tips like using cleansers, moisturizers, sunscreens, or diets.
        - Only suggest **clinical treatments, prescription medications, or dermatologist visits** if necessary.
        - If no doctor consultation is required, state that clearly.

        Should I see a dermatologist? If yes, what medical treatments should I consider?
        """
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
        response = model.generate_content(prompt)

        return response.text if response and hasattr(response, "text") else "Consult a dermatologist for more details."
    except Exception as e:
        return f"AI Error: {str(e)}"
