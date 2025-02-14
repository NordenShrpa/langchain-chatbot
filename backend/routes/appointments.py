from fastapi import APIRouter, HTTPException
from backend.services.appointment_service import book_appointment, get_appointments

router = APIRouter()

@router.post("/book")
async def book_appointment_endpoint(user_id: str, user_input: str):
    """Handles appointment booking."""
    try:
        response = book_appointment(user_id, user_input)
        return {"message": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/appointments")
async def get_appointments_endpoint():
    """Fetches all appointments."""
    try:
        appointments = get_appointments()
        return {"appointments": appointments}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
