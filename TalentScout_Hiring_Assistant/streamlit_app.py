import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Google Generative AI
genai.configure(api_key=GOOGLE_API_KEY)
MODEL_NAME = "gemini-1.5-flash"  # Ensure this model is available in your API region

# Function to interact with AI
def chat_with_ai(prompt):
    try:
        if any(word in prompt.lower() for word in ["exit", "quit", "bye"]):
            return "Thank you for using TalentScout Hiring Assistant. Goodbye!"

        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="TalentScout Hiring Assistant", layout="centered")
st.title("TalentScout Hiring Assistant")
st.subheader("AI-Powered Candidate Screening")

# Collect Candidate Information
with st.form("candidate_form"):
    st.subheader("Candidate Information")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.number_input("Years of Experience", min_value=0)
    position = st.text_input("Position Applied For")
    location = st.text_input("Current Location")
    tech_stack = st.text_input("Candidate's Tech Stack (comma-separated)")
    submit_button = st.form_submit_button("Generate Interview Questions")

if submit_button:
    if name and email and phone and tech_stack:
        st.success(f"Candidate {name} is applying for {position}. Generating questions...")

        prompt = (
            f"Generate 5 technical interview questions for a candidate applying for {position}. "
            f"The candidate is skilled in {tech_stack} and has {experience} years of experience."
        )
        questions = chat_with_ai(prompt)

        st.subheader("Generated Interview Questions:")
        st.write(questions)
    else:
        st.warning("Please fill in all required fields.")

# Conversation Exit Message
if st.button("Exit Chat"):
    st.write("Thank you for using TalentScout Hiring Assistant. Goodbye!")