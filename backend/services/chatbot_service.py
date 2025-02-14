from langchain_google_genai import GoogleGenerativeAI
import os
from backend.services.user_service import collect_user_info
from backend.services.user_service import extract_user_info  

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini LLM
llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API_KEY)

def process_query(query: str):
    """Uses Gemini API to generate a chatbot response."""
    if "call me" in query.lower():
        name, email, phone = extract_user_info(query)  
        return collect_user_info(name, email, phone)  
    return llm.generate_text(query)
