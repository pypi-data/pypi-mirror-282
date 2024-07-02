import os
import subprocess
import sys
import fitz  # PyMuPDF
from pdf2image import convert_from_path
import pytesseract
from langchain_community.chat_models import ChatOllama
import streamlit as st

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as pdf_document:
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                text += page.get_text()
    except Exception as e:
        print(f"Error opening or reading PDF: {e}")
    return text

def ocr_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    ocr_text = ""
    for page in pages:
        ocr_text += pytesseract.image_to_string(page)
    return ocr_text

def extract_text_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        return file.read()

def chat_with_doc(model_name, file_path, use_gui=False):
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
        if not text:
            text = ocr_pdf(file_path)
    elif file_path.endswith('.txt'):
        text = extract_text_from_txt(file_path)
    else:
        print("Unsupported file type. Please provide a PDF or TXT file.")
        return

    llm = ChatOllama(model=model_name, temperature=0.9)
    chat_history = []

    if use_gui:
        st.title("Chat with Document Content")
        user_input = st.chat_input("Ask a question:")
        if user_input:
            chat_history.append(("human", user_input))
            prompt = f"Based on the following document content, explain the code:\n{text}\n\nHuman: {user_input}"
            response = llm.invoke(prompt, context=text)
            chat_history.append(("assistant", response.content))
            st.write(response.content)
    else:
        user_input = "What is the main topic of this document?"
        chat_history.append(("human", user_input))
        prompt = f"Based on the following document content, explain the code:\n{text}\n\nHuman: {user_input}"
        response = llm.invoke(prompt, context=text)
        print("Response:", response.content)

if __name__ == "__main__":
    if __name__ == "__main__" and not os.environ.get("STREAMLIT_RUNNING"):
        os.environ["STREAMLIT_RUNNING"] = "true"
        subprocess.run(["streamlit", "run", __file__] + sys.argv[1:])
        sys.exit()
    chat_with_doc("gemma:2b", "data.txt", use_gui=True)
