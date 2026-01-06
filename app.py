import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")

# 🎵 App Title
st.title("🎶 Song Recommend System 🎶")

# Intro Section
st.markdown("---")
st.header("✨ Welcome to Your Mood-Based DJ ✨")
st.markdown("Tell me how you feel, and I'll suggest songs that vibe with your mood.")
st.markdown("---")

# User Input
st.subheader("📝 Enter Your Mood Below")
raw_input = st.text_input("Mood (e.g., happy, sad, energetic, relaxed):")

# Normalize input: strip spaces and convert to lowercase
user_input = raw_input.strip().lower()


# Submit Button
submit_button = st.button("🎧 Get Recommendations")

# Response Section
if submit_button:
    if user_input:
        response = model.generate_content(
            f"Recommend top 5 songs that match the following mood: {user_input} "
            f"with their artists names in a tabular format."
        )
        st.markdown("---")
        st.subheader("🎤 Recommended Songs")
        st.write(response.text)
        st.markdown("---")
        st.markdown("Enjoy your playlist! 🎵")
    else:
        st.warning("⚠️ Please enter your mood and click the button to get recommendations.")