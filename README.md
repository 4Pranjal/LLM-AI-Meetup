# Gemini-Powered Chatbot Application

This repository contains multiple Streamlit applications powered by Google Gemini models for different use cases such as PDF-based Q&A and image processing. These apps leverage Google Generative AI and Langchain for language models and embedding generation.

## Features

- **Q&A Chatbot**: Ask questions and get responses from Google Gemini models, with or without chat history saving.
- **PDF Chatbot**: Upload PDF files and ask questions based on the content of the PDF.
- **Image Processing**: Use the Gemini model to process images and get descriptions.

## Project Structure

- `chatpdf.py` and `chatpdf2.py`: Streamlit apps for interacting with PDFs.
- `qachat1.py` and `qachat2.py`: Q&A chatbots. `qachat2.py` includes chat history storage.
- `vision.py`: Streamlit app for image-based interaction using Google Gemini.
- `test.py`: Script to list available Google Gemini models.
- `requirements.txt`: List of required Python packages.

## Installation

To run these applications, follow these steps:

### 1. Clone the repository
 
git clone https://github.com/4Pranjal/LLM-AI-Meetup

## 2. Set up a Python virtual environment (optional but recommended)
python3 -m venv venv
On Windows use `venv\Scripts\activate`

## 3. Install dependencies
Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 4. Set up environment variables
Create a .env file in the root directory of your project.
Inside this file, set your Google API key:

GOOGLE_API_KEY=your_google_api_key_here
You can get your API key from the Google Cloud Console.

## 5. Run the applications
You can run each application by navigating to the project folder and executing the following command:

For Q&A Chatbot (without history saving):
   ```bash
   streamlit run qachat1.py
   ```
For Q&A Chatbot (with history saving):
   ```bash
   streamlit run qachat2.py
   ```
streamlit run qachat2.py
For PDF Chatbot:
   ```bash
   streamlit run chatpdf.py
   ```
   ```bash
   streamlit run qachat2.py
   ```

For Image Processing Demo:
   ```bash
   streamlit run vision.py
   ```
streamlit run vision.py

## Contributors

- [Pranjal Jain](https://github.com/4Pranjal)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


