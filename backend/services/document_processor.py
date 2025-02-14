import os
import fitz  # PyMuPDF for PDFs
import docx
import pandas as pd
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file"""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(docx_path):
    """Extract text from a DOCX file"""
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_csv(csv_path):
    """Extract text from a CSV file (converting it to a string format)"""
    df = pd.read_csv(csv_path)
    return df.to_string()

def process_documents():
    """Load and process documents from the 'documents' folder"""
    docs_path = "backend/documents/"
    all_texts = []

    for file in os.listdir(docs_path):
        file_path = os.path.join(docs_path, file)
        if file.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                all_texts.append(f.read())
        elif file.endswith(".pdf"):
            all_texts.append(extract_text_from_pdf(file_path))
        elif file.endswith(".docx"):
            all_texts.append(extract_text_from_docx(file_path))
        elif file.endswith(".csv"):
            all_texts.append(extract_text_from_csv(file_path))

    # Convert extracted text into embeddings and store in FAISS
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(all_texts, embeddings)
    vector_store.save_local("backend/vector_store")
    print("Documents processed and indexed successfully!")

if __name__ == "__main__":
    process_documents()
