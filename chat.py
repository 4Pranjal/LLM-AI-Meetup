import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Google Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini Model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Function to get Gemini response for a given question
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Set up the Streamlit app -- Front end ---->>>>>
st.set_page_config(page_title="Gemini Q&A Application")

# App header
st.header("Q&A Chatbot with Gemini 💬")

# Text input for the user to ask questions
user_input = st.text_input("Ask a Question:", key="input")

# Submit button for asking the question
submit = st.button("Submit")

# If the submit button is clicked, generate and display the response
if submit:
    if user_input:
        response = get_gemini_response(user_input)

        # Display the response in chunks (since the response is streamed)
        st.subheader("Response:")
        for chunk in response:
            st.write(chunk.text)
        
        # Display the chat history
        st.subheader("Chat History")
        st.write(chat.history)
    else:
        st.warning("Please enter a question before submitting.")
