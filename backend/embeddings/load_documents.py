from langchain.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", google_api_key=GEMINI_API_KEY
)

vector_db = FAISS(embedding_function=embeddings)

def load_and_index_documents():
    """Loads PDFs, TXT, and CSV files and indexes them in FAISS."""
    doc_files = ["documents/sample.pdf", "documents/sample.txt", "documents/sample.csv"]

    
    for file in doc_files:
        if file.endswith(".pdf"):
            loader = PyPDFLoader(file)
        elif file.endswith(".txt"):
            loader = TextLoader(file)
        elif file.endswith(".csv"):
            loader = CSVLoader(file)
        else:
            continue

        docs = loader.load()
        vector_db.add_documents(docs)

    print("Documents successfully indexed!")

if __name__ == "__main__":
    load_and_index_documents()
