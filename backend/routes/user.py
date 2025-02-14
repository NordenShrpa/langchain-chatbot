from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import User
from pydantic import BaseModel, EmailStr
import uuid

router = APIRouter()

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str

@router.post("/register/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(id=str(uuid.uuid4()), name=user.name, email=user.email, phone=user.phone)
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully!", "user_id": new_user.id}