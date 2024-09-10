import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import json
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize session state for chat history and previous response
if "chat_history" not in st.session_state:
    # Load history from a file if it exists
    try:
        with open("chat_history.json", "r") as file:
            st.session_state.chat_history = json.load(file)
    except FileNotFoundError:
        st.session_state.chat_history = []

if "previous_response" not in st.session_state:
    st.session_state.previous_response = None

# Function to save the chat history to a file
def save_history():
    with open("chat_history.json", "w") as file:
        json.dump(st.session_state.chat_history, file)

# Function to extract text from uploaded PDF documents
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to split the extracted text into chunks for processing
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create and save a vector store from text chunks using embeddings
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# Function to create a conversational chain with a specific prompt template
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context. Make sure to provide all the details. 
    If the answer is not in the provided context, just say, "Answer is not available in the context." 
    Don't provide an incorrect answer.

    Context:\n{context}\n
    Question:\n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Function to handle user input, perform a similarity search, and generate a response
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

    docs = vector_store.similarity_search(user_question)
    chain = get_conversational_chain()

    # Generate the response from the question and context documents
    response = chain(
        {"input_documents": docs, "question": user_question}, return_only_outputs=True
    )

    # Store the current response in the session state for future history storage
    st.session_state.previous_response = {"question": user_question, "response": response["output_text"]}

    # Display the response with a copy button
    st.write("Reply:", response["output_text"])
    st.button("Copy Response", key=f"copy_{user_question}", on_click=st.experimental_set_query_params, kwargs={"text": response["output_text"]})

# Main function to build the Streamlit app UI
def main():
    st.set_page_config("Chat PDF")
    st.header("Chat with PDF using Gemini 💁")

    # Input field for user question with a button near the input field
    user_question = st.text_input("Ask a Question from the PDF Files")
    submit_question = st.button("Submit Question")

    if submit_question and user_question:
        # Save the previous response to history before generating the new response
        if st.session_state.previous_response:
            st.session_state.chat_history.append(st.session_state.previous_response)

        # Generate the response for the current question
        user_input(user_question)

        # Save the updated chat history to a file
        save_history()

    # Sidebar for file uploading and processing
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)

        process_button = st.button("Submit & Process")
        if process_button and pdf_docs:
            with st.spinner("Processing..."):
                # Process the uploaded PDFs
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Processing completed!")

    # Display chat history
    st.subheader("Chat History")
    if st.session_state.chat_history:
        for idx, chat in enumerate(st.session_state.chat_history):
            st.write(f"**Q:** {chat['question']}")
            st.write(f"**A:** {chat['response']}")
            # Add a copy button for each response
            st.button("Copy", key=f"copy_{idx}", on_click=st.experimental_set_query_params, kwargs={"text": chat["response"]})

# Entry point of the application
if __name__ == "__main__":
    main()
