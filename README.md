# 🌿 DermaAI – AI-Powered Skincare Advisor  

### *Unlock Your Perfect Skin with AI-Driven Insights*  

DermaAI is an *AI-powered skincare recommendation app* that provides personalized skincare advice, weather-based tips, diet recommendations, and home remedies. It also offers *doctor consultation suggestions* and *product recommendations. One of its **unique features* is *skin image analysis using OpenCV*, which helps users assess their skin health by analyzing images.  

*🔗 Live Demo:* [DermaAI](https://derma-ai.streamlit.app/)  

---

## 🛠 Tech Stack  

| Component          | Technology Used                                  |
|--------------------|--------------------------------------------------|
| *Frontend*       | Streamlit (Python-based UI)                      |
| *AI Model*       | Gemini API (AI-powered skincare analysis & advice) |
| *Weather API*    | OpenWeatherMap API (for weather-based skincare recommendations) |
| *Dataset*        | Amazon Beauty Products Dataset (Kaggle)         |
| *Image Analysis* | OpenCV (for skin condition assessment)           |

---

## ✨ Key Features  

### 🔹 1. AI-Based Skincare Advice  
- Uses *Gemini AI* to provide *custom skincare routines*.  
- *Benefits*:  
  - Personalized skincare based on *age, gender, skin type, and concerns*.  
  - *Morning & night routine recommendations* tailored to user needs.  

### 🔹 2. Weather-Based Skincare Recommendations  
- Fetches *live weather data* using *OpenWeatherMap API*.  
- *Benefits*:  
  - Adjusts skincare tips for *temperature, humidity, and UV index*.  
  - Helps prevent *sun damage, dryness, and excess oil*.  

### 🔹 3. Personalized Diet Plans  
- AI suggests *nutrition plans* for better skin health.  
- *Benefits*:  
  - Helps with *acne, dryness, and aging*.  
  - Advises on *hydration, vitamins, and skin-friendly foods*.  

### 🔹 4. Home Remedies Generator  
- AI suggests *natural remedies* based on skin concerns.  
- *Benefits*:  
  - Uses *ingredients from home* for skincare.  
  - Offers *safe, chemical-free* solutions.  

### 🔹 5. Doctor Consultation Suggestions  
- AI *analyzes symptoms* and suggests *dermatologist consultation* if needed.  
- *Benefits*:  
  - Helps identify *serious skin conditions*.  
  - Connects users with *dermatology resources*.  

### 🔹 6. Skincare Product Recommendations  
- Uses the *Amazon Beauty Products dataset* for product recommendations.  
- *Benefits*:  
  - Suggests *top-rated skincare products*.  
  - Direct links to trusted *brands & sellers*.  

### 🔹 7. *Skin Image Analysis (Unique Feature!)*  
- Uses *OpenCV* to analyze *JPG, PNG, JPEG* images.  
- *Detects:*  
  - *Blemish Percentage*  
  - *Skin Tone & Condition*  
  - *Pore Visibility*  
- *Benefits*:  
  - AI-powered *self-diagnosis* of skin health.  
  - Helps track *skin improvement over time*.  

---

## 📂 Project Structure

```bash
DermaAI/
│── .gitignore                  # Ignore unnecessary files
│── app.py                      # Main Streamlit app
│── ai_recommendations.py       # AI skincare advice using Gemini API
│── diet_recommendations.py     # Nutrition-based skincare advice
│── doctor_consultation.py      # Doctor consultation suggestion
│── home_remedies_ai.py         # AI-generated home remedies
│── product_api.py              # Fetches skincare product recommendations
│── skin_analysis_opencv.py     # Skin image analysis using OpenCV
│── weather_api.py              # Fetches weather data
│── cleaned_skincare_products.csv.gz # Compressed skincare product dataset
│── compress_csv.py             # Script to compress dataset
│── requirements.txt            # Python dependencies
