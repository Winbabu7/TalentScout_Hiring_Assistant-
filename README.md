# TalentScout_Hiring_Assistant-
Project Overview

TalentScout Hiring Assistant is an AI-powered chatbot designed to assist in the initial screening of candidates for technology placements. It gathers essential candidate details and generates relevant technical questions based on the declared tech stack.

Features

Candidate Information Gathering

Full Name

Email Address

Phone Number

Years of Experience

Desired Position

Current Location

Tech Stack (Programming languages, frameworks, databases, etc.)


AI-Generated Technical Questions

Generates 3-5 interview questions based on the candidate’s tech stack.

Ensures questions are relevant and appropriately challenging.


Conversation Flow Handling

Maintains context for follow-up questions.

Provides meaningful responses for unexpected inputs.

Ends conversations gracefully with next-step guidance.



Tech Stack

Frontend: Streamlit

AI Model: Gemini API (Google Generative AI)

Backend: Python

Version Control: Git, GitHub


Installation Instructions

1. Clone the Repository

git clone https://github.com/Winbabu7/TalentScout_Hiring_Assistant.git
cd TalentScout_Hiring_Assistant

2. Create a Virtual Environment

python -m venv venv

Activate the virtual environment:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate


3. Install Dependencies

pip install -r requirements.txt

4. Set Up API Key

1. Create a .env file in the project folder.


2. Add your Google API key:



GOOGLE_API_KEY=your_api_key_here

5. Run the Application

streamlit run streamlit_app.py

Usage Guide

1. Enter candidate details in the UI.


2. Provide the tech stack to generate relevant interview questions.


3. Click "Generate Interview Questions" to get AI-generated questions.


4. Review the questions and use them for the hiring process.



Deployment

The application can be deployed locally.

For cloud deployment, services like Streamlit Sharing, GCP, or AWS can be used.


Project Structure

TalentScout_Hiring_Assistant/
│── .env                  # Environment variables (API key)  
│── streamlit_app.py       # Main Streamlit app  
│── requirements.txt       # Python dependencies  
│── README.md              # Project documentation  
│── .gitignore             # Git ignore file
