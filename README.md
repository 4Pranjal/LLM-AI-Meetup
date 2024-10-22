# 🚀 LLM-AI-Meetup: Google Gemini-Powered Apps

Welcome to the **LLM-AI-Meetup** repository! This project contains multiple **Streamlit** applications powered by **Google Gemini** models for various tasks like Q&A, PDF content interaction, and image processing. Explore the power of cutting-edge AI technology! 🤖✨

## 🌟 Features
- **🗨️ Q&A Chatbot**: Ask questions and get responses from Google Gemini models, with or without chat history saving.
- **📄 PDF Chatbot**: Upload PDF files and ask questions based on their content.
- **🖼️ Image Processing**: Use the Gemini model to process images and get descriptions.
- **🌐 Web Scraping**: Extract information from websites using the Gemini model.

## 📁 Project Structure
```plaintext
📂 LLM-AI-Meetup/
 ┣  ChatPDF/
 ┃ ┣  chatpdf.py           # Streamlit app for PDF interaction
 ┃ ┗  chatpdf2.py          # Another variant for PDF Q&A
 ┣  Q&A/
 ┃ ┣  qachat1.py           # Q&A chatbot without history saving
 ┃ ┗  qachat2.py           # Q&A chatbot with history saving
 ┣  Vision/
 ┃ ┗  vision.py            # Streamlit app for image-based interaction using Google Gemini
 ┣  test.py                # Script to list available Google Gemini models
 ┣  requirements.txt        # List of required Python packages
 ┗  README.md               # Project documentation

```

## Installation

To run these applications, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/4Pranjal/LLM-AI-Meetup
```
## 2. Set up a Python virtual environment 
   ```bash
   python3 -m venv venv
   ```
or you can use conda to create environment.
On Windows use
   ```bash
venv\Scripts\activate
   ```

## 3. Install dependencies
Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 4. Set up environment variables
Create a .env file in the root directory of your project.
Inside this file, set your Google API key:
   ```bash
GOOGLE_API_KEY=your_google_api_key_here
   ```
You can get your API key from the Google Cloud Console.

## 5. Run the applications
You can run each application by navigating to the project folder and executing the following command:
Open the directoryc for Q&A Chatbot:-
   ```bash
   cd Q&A
   ```
Run the python script file
For Q&A Chatbot (without history saving):
   ```bash
   streamlit run Q&A-v.1.py
   ```
For Q&A Chatbot (with history saving):
   ```bash
   streamlit run Q&A-v.2.py
   ```
---
Open the directory for ChatPDF:-
   ```bash
   cd ChatPDF
   ```
For PDF Chatbot:
   ```bash
   streamlit run ChatPDF.py
   ```
   ```bash
   streamlit run ChatPDF-v.2.py
   ```
---
For Image Processing Demo:
Open the directory for Vision:-
   ```bash
   cd Vision
   ```
Run the Python Script
   ```bash
   streamlit run vision.py
   ```

## 🙏 Contributors

This repository is maintained by 4Pranjal. Feel free to use and modify the code for educational and research purposes.

For any questions or suggestions, you can contact me through my GitHub profile: [@4Pranjal](https://github.com/4Pranjal).

Made with ❤️ by [Pranjal Jain](https://github.com/4Pranjal)



