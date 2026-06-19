# 🌱 AgriProtect: AI for Sustainability
**AgriProtect** is an accessible, multimodal agricultural diagnostic tool designed to empower small-scale farmers in India. By leveraging Generative AI and computer vision, AgriProtect diagnoses crop diseases in real-time and prioritizes locally available, cost-effective organic remedies over harmful chemical pesticides.
This project was developed as part of the **1M1B & IBM SkillsBuild AI for Sustainability Internship**.
## 🎯 The Problem
Small-scale farmers often lack immediate access to professional agronomists. When crops show signs of disease, farmers frequently rely on pesticide vendors for advice, resulting in the over-application of expensive, broad-spectrum chemical pesticides. This creates a cycle of financial loss, soil degradation, and environmental pollution.
## 💡 The Solution
AgriProtect acts as an "honest agronomist in your pocket." Farmers can snap a picture of a diseased leaf and describe the symptoms using voice or text. The app uses **Google Gemini 2.5 Flash** (Multimodal AI) to analyze the visual and textual data, strictly prioritizing eco-friendly, organic treatments (like neem oil or buttermilk solutions) to save the farmer money and protect the environment.
## ✨ Key Features
 * **📸 Multimodal Diagnostics:** Upload images, take a live picture, use voice-to-text, or type symptoms.
 * **🧠 AI Vision Model:** Powered by Google Gemini 2.5 Flash to visually analyze leaf damage and disease patterns.
 * **🌿 Organic-First Recommendations:** Prompt-engineered to suggest zero-to-low-cost organic treatments before resorting to chemicals.
 * **🗣️ High Accessibility:** Built with an intuitive, mobile-responsive UI using Streamlit, requiring minimal technical literacy.
## 🌍 UN Sustainable Development Goals (SDGs) Addressed
 * **SDG 2: Zero Hunger** (Mitigating crop loss and boosting yields)
 * **SDG 12: Responsible Consumption and Production** (Reducing toxic chemical pesticide usage)
 * **SDG 1: No Poverty** (Saving farmers money by lowering input costs)
 * **SDG 15: Life on Land** (Preventing chemical runoff and protecting soil health)
## 🛠️ Tech Stack
 * **Frontend & Web Framework:** Streamlit
 * **AI Backend:** Google Generative AI (gemini-2.5-flash)
 * **Language:** Python 3.9+
 * **Image Processing:** Pillow (PIL)
## 🚀 How to Run Locally
### 1. Clone the Repository
```bash
git clone [https://github.com/YourUsername/AgriProtect.git](https://github.com/YourUsername/AgriProtect.git)
cd AgriProtect

```
### 2. Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt

```
### 3. Get a Google Gemini API Key
 * Go to Google AI Studio.
 * Sign in with your Google account and click **Get API Key**.
 * Create a new API key and copy it.
### 4. Setup Secrets
Create a .streamlit folder inside your project directory, and inside it, create a file named secrets.toml. Add your API key like this:
```toml
GOOGLE_API_KEY = "your_copied_api_key_here"

```
### 5. Run the Application
```bash
streamlit run crop_ai_app.py

```
The application will open automatically in your web browser!
## 🌐 Deployment
This application is designed to be easily deployed on **Streamlit Community Cloud**.
 1. Connect your GitHub repository to Streamlit Cloud.
 2. Set the main file path to crop_ai_app.py.
 3. Paste your GOOGLE_API_KEY into the Streamlit Advanced Settings -> Secrets manager.
 4. Click Deploy!
 5. 
