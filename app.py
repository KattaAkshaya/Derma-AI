import streamlit as st
from ai_recommendations import get_ai_recommendations  
from product_api import fetch_products_from_dataset
from weather_api import get_weather, skincare_recommendations
from diet_recommendations import get_diet_recommendations
from skin_analysis_opencv import analyze_skin_opencv
from doctor_consultation import suggest_doctor
from home_remedies_ai import get_home_remedies
import os
from dotenv import load_dotenv

# ✅ Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

st.set_page_config(page_title="🧠💆‍♀️DermaAI", layout="wide")



# Custom CSS for Styling Output Cards
st.markdown("""
    <style>
        
        /* Main Layout */
        .main-container {
            display: grid;
            grid-template-columns: 1fr 3fr;
            gap: 20px;
            width: 100%;
            transition: all 0.3s ease-in-out;
        }

        @media (max-width: 1000px) {
            .main-container {
                grid-template-columns: 1fr;
            }
        }

        /* Title Styling */
        .title-container {
            text-align: center;
            animation: fadeIn 1.2s ease-in-out;
        }

        h1 {
            font-size: 2rem;
            color: #4CAF50;
            margin-bottom: 5px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }

        .tagline {
            font-size: 1.2rem;
            color:#B0B0B0;
            font-weight: 500;
        }

        /* Button Styling */
        .stButton > button {
            background-color: #6BCB77;
            color: white;
            font-size: 18px;
            padding: 12px;
            width: 80%;
            border-radius: 8px;
            transition: 0.3s ease-in-out;
        }

        .stButton > button:hover {
            background-color: #4CAF50;
            transform: scale(1.05);
        }

        @media (max-width: 1200px) {
            .stButton > button {
                font-size: 16px;
                width: 100%;
            }
        }

        /* Custom Output Cards */
        .custom-card {
            padding: 15px;
            border-radius: 12px;
            box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.2);
            margin: 15px 0;
            font-size: 16px;
            font-weight: 500;
            text-align: center;
            
            transition: transform 0.3s ease-in-out;
        }

        .custom-card:hover {
            transform: translateY(-5px);
            box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.25);
        }

        .custom-card h3 {
            color: #4CAF50;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .product-button {
                    display: inline-block;
                    background-color: #4CAF50;
                    color: white !important;;
                    padding: 10px 15px;
                    border-radius: 5px;
                    text-decoration: none !important;
                    font-size: 16px;
                    font-weight: bold;
                    transition: background 0.3s ease-in-out;
                }
                .product-button:hover {
                    background-color: #45a049;
                }
            
    </style>
""", unsafe_allow_html=True)

  
# Page Title
st.markdown('<div class="title-container"><h1>🧠💆‍♀️DermaAI</h1><p class="tagline">✨ Unlock your perfect skin with AI-powered advice ✨</p></div>', unsafe_allow_html=True)

# Main Layout
st.markdown('<div class="main-container">', unsafe_allow_html=True)


# Sidebar: User Inputs (Includes Image Upload)
with st.sidebar:
    
    gender = st.selectbox("Select your gender:", ["Male", "Female", "Non-Binary", "Prefer not to say"])
    skin_type = st.selectbox("Select your skin type:", ["Oily", "Dry", "Combination", "Sensitive", "Normal"])
    age = st.number_input("Enter your age:", min_value=10, max_value=100, step=1)
    city = st.text_input("🌍 Enter your city for weather-based skincare recommendations:")
    user_input = st.text_area("✍️ Describe your skin concerns (e.g., acne, dark spots, wrinkles):")

    # 📸 Upload Skin Image (Moved inside Personal Details)
    uploaded_image = st.file_uploader("📸 Upload a skin image for analysis", type=["jpg", "png", "jpeg"])


    
# Skin Image Analysis (If Uploaded)
if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Skin Image", use_container_width=True)
    
    with st.spinner("Analyzing your skin..."):
        analysis_result = analyze_skin_opencv(uploaded_image)

    st.markdown(f"""
        <div class="custom-card">  
            <h3>✅ Skin Analysis Results</h3>
            <p><b>Skin Tone:</b> {analysis_result.get('skin_tone', 'Not Detected')}</p>
            <p><b>Condition:</b> {analysis_result.get('condition', 'Not Detected')}</p>
            <p><b>Blemish Percentage:</b> {analysis_result.get('blemish_percentage', 0.00):.2f}%</p>
            <p><b>Oiliness:</b> {analysis_result.get('oiliness', 'Not Detected')}</p>
            <p><b>Dryness:</b> {analysis_result.get('dryness', 'Not Detected')}</p>
            <p><b>Hyperpigmentation:</b> {analysis_result.get('hyperpigmentation', 'Not Detected')}</p>
            <p><b>Wrinkles:</b> {analysis_result.get('wrinkles', 'Not Detected')}</p>
            <p><b>Pore Size:</b> {analysis_result.get('pores', 'Not Detected')}</p>
            <p><b>Texture:</b> {analysis_result.get('texture', 'Not Detected')}</p>
            <p><b>Dark Circles:</b> {analysis_result.get('dark_circles', 'Not Detected')}</p>
            <p><b>UV Damage:</b> {analysis_result.get('uv_damage', 'Not Detected')}</p>
        </div>
    """, unsafe_allow_html=True)

# Main Content
st.markdown('<div class="content">', unsafe_allow_html=True)

# AI-Powered Skincare Advice Button ✅
if st.button("🤖 Get AI-Powered Skincare Advice"):
    with st.spinner("Generating AI-powered skincare recommendations..."):
        ai_advice = get_ai_recommendations(user_input, skin_type,gender,age)

    if ai_advice:
        st.subheader("💡 AI-Powered Skincare Advice")
        st.markdown(f"""
            <div class="custom-card">
                <p>{ai_advice}</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("❌ Unable to generate AI advice. Try again.")
        

# Weather-Based Skincare Advice ✅
if st.button("🌦️ Get Weather-Based Skincare Advice"):
    if city:
        with st.spinner(f"Fetching weather details for {city}..."):
            weather_info = get_weather(city)

        if "error" not in weather_info:
            weather_advice = skincare_recommendations(skin_type, weather_info,user_input)

            st.subheader("🌦️ Weather-Based Skincare Advice")
            st.markdown(f"""
                <div class="custom-card">
                    <p><b>Weather:</b> {weather_info['condition']}</p>
                    <p><b>Temperature:</b> {weather_info['temperature']}°C</p>
                    <p><b>Humidity:</b> {weather_info['humidity']}%</p>
                    <p>{weather_advice}</p>
                </div>
            """, unsafe_allow_html=True)
            
        else:
            st.error("❌ No weather data available. Try again.")
    else:
        st.warning("⚠️ Please enter your city first.")


# Diet-Based Skincare Recommendations ✅
if st.button("🥗 Get Diet Recommendations"):
    with st.spinner("Generating personalized diet plan..."):
        diet_plan = get_diet_recommendations(skin_type,age,user_input,gender)

    if diet_plan:
        st.subheader("🍎 Personalized Diet for Better Skin")
        st.markdown(f"""
            <div class="custom-card">
                <p>{diet_plan}</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("❌ Unable to generate diet recommendations.")
   
    
# Home Remedies for Skincare ✅
if st.button("🌿 Get Home Remedies"):
    with st.spinner("Fetching natural skincare remedies..."):
        home_remedy = get_home_remedies(user_input, skin_type,gender,age)

    if home_remedy:
        st.subheader("🌿 Natural Home Remedies")
        st.markdown(f"""
            <div class="custom-card">
                <p>{home_remedy}</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("❌ No home remedies found.")
   
# Doctor Consultation Suggestion ✅
if st.button("🩺 Get Doctor Consultation Advice"):
    with st.spinner("Analyzing skin concerns for doctor recommendation..."):
        doctor_suggestion, detailed_advice = suggest_doctor(skin_type=skin_type, user_input=user_input, age=age)

    # Display Results
    if doctor_suggestion:
        st.subheader("🩺 Doctor Consultation Suggestion")
        st.markdown(f"""
            <div class="custom-card">
                <p>{doctor_suggestion}</p>
            </div>
        """, unsafe_allow_html=True)

        if detailed_advice:
            st.subheader("📝 AI-Powered Dermatology Advice")
            st.markdown(f"""
                <div class="custom-card">
                    <p>{detailed_advice}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("✅ No urgent doctor consultation needed. Follow a proper skincare routine.")
    
# Skincare Product Recommendations Button ✅
if st.button("🔍 Get Product Recommendations"):
    with st.spinner("Fetching skincare products..."):
        recommended_products = fetch_products_from_dataset(skin_type, user_input)

    if not recommended_products.empty:
        st.subheader("🛍️ Recommended Skincare Products")

        for _, row in recommended_products.iterrows():
            st.markdown(f"""
                <div class="custom-card">
                    <h3>🔹 {row['ProductId']}</h3> 
                    <p>🛒 <b>Type:</b> {row['ProductType']}</p>
                    <p>⭐ <b>Rating:</b> {row['Rating']} / 5</p>
                   <a href='{row['URL']}' target='_blank' class="product-button">🛍️ View Product</a>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.error("❌ No matching products found. Try refining your skin concerns.")


# Close Main Container
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
