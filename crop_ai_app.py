import streamlit as st
import time
from streamlit_mic_recorder import speech_to_text
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="AgriProtect AI", page_icon="🌾", layout="centered")

st.title("🌿 AgriProtect: Local Crop Assistant")
st.markdown("Identify crop diseases and get local organic remedies instantly using Google Gemini.")

# ==========================================
# 1. SECRETS CONFIGURATION (GEMINI)
# ==========================================
try:
    gemini_api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=gemini_api_key)
except KeyError:
    st.error("⚠️ Secrets not found! If running locally, check your .streamlit/secrets.toml file. If on Streamlit Cloud, check the Advanced Settings.")
    st.stop()

# ==========================================
# 2. CORE APPLICATION LOGIC
# ==========================================
st.subheader("📋 Step 1: Identify Crop")

col1, col2 = st.columns([5, 2])
with col2:
    st.write("🎙️ Speak Crop")
    crop_voice = speech_to_text(language='en', use_container_width=True, just_once=True, key='crop_mic')
with col1:
    crop_type = st.text_input(
        "Enter Crop Name (e.g., Wheat, Mango, Sugarcane):", 
        value=crop_voice if crop_voice else ""
    )

st.subheader("🔍 Step 2: Provide Symptoms")
st.markdown("Choose how you want to describe the issue:")

tab1, tab2 = st.tabs(["🗣️ Voice & Text", "📸 Upload Image / Camera"])

with tab1:
    col3, col4 = st.columns([5, 2])
    with col4:
        st.write("🎙️ Speak Symptoms")
        symptoms_voice = speech_to_text(language='en', use_container_width=True, just_once=True, key='symptoms_mic')
    with col3:
        symptoms_text = st.text_area(
            "Describe what you see on the plant:", 
            value=symptoms_voice if symptoms_voice else ""
        )

with tab2:
    st.markdown("Take a picture or upload an image of the diseased crop. 🌾")
    uploaded_image = st.file_uploader("Upload an image (JPG, PNG)", type=["jpg", "jpeg", "png"])
    camera_image = st.camera_input("Or take a picture directly")
    
    final_image_file = uploaded_image or camera_image
    
    if final_image_file:
        st.image(final_image_file, caption="Uploaded Crop Image", use_container_width=True)
        st.success("Image received! Gemini Vision will analyze this.")

st.markdown("---")

# ==========================================
# 3. ANALYSIS & RAG EXECUTION (VIA GEMINI)
# ==========================================
if st.button("🚀 Analyze with Google Gemini (Vision & RAG Enabled)"):
    if not crop_type:
        st.warning("⚠️ Please enter the crop name in Step 1.")
    elif not symptoms_text and not final_image_file:
        st.warning("⚠️ Please either describe the symptoms or upload an image in Step 2.")
    else:
        with st.spinner("Analyzing symptoms & retrieving local organic guidelines using Gemini..."):
            try:
                # Setup Gemini Model (Gemini 1.5 Flash is incredibly fast and multimodal)
                model = genai.GenerativeModel("gemini-2.5-flash")
                
                # Dynamic Prompt forcing SDG 12 and organic focus
                prompt = f"""
                You are an expert agricultural AI assistant working in India. 
                Crop Name: {crop_type}
                Farmer's reported symptoms: {symptoms_text if symptoms_text else "None provided by text. Rely solely on the image."}
                
                Task:
                1. Identify the likely disease.
                2. Recommend an organic, locally available remedy in India (e.g., Neem oil, Buttermilk). 
                3. Provide the estimated financial savings per acre by avoiding commercial chemicals.
                4. Include a warning that chemicals should only be a last resort.
                
                Please format your response nicely using Markdown (bullet points, bold text). Do NOT use conversational filler, just output the analysis.
                """
                
                # If image exists, pass both image and text to Gemini!
                if final_image_file:
                    img = Image.open(final_image_file)
                    response = model.generate_content([prompt, img])
                else:
                    response = model.generate_content(prompt)
                
                st.success("Analysis Complete!")
                
                # --- DISPLAY DASHBOARD RESULTS ---
                st.subheader(f"🦠 Disease Analysis for {crop_type}")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")
