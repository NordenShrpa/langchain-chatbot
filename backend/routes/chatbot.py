from fastapi import APIRouter, HTTPException
from backend.services.chatbot_service import process_query

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(query: str, user_info: dict = None):
    """Handles chatbot queries."""
    try:
        if user_info:
            response = process_query(query, user_info)
        else:
            response = process_query(query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
