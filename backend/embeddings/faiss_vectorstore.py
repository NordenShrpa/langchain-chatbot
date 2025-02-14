from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
import faiss
import numpy as np
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Load Gemini Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", google_api_key=GEMINI_API_KEY
)

# Initialize FAISS Vectorstore
vector_db = FAISS(embedding_function=embeddings)

def embed_text(text: str):
    """Converts text into embeddings."""
    return embeddings.embed_documents([text])[0]

def retrieve_answer(query: str):
    """Retrieves the best matching document for a user query."""
    query_embedding = embed_text(query)
    distances, indices = faiss.IndexFlatL2(768).search(
        np.array([query_embedding], dtype=np.float32), k=1
    )
    return vector_db.documents[indices[0][0]] if indices[0][0] != -1 else "No relevant answer found."
