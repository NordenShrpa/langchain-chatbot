from fastapi import FastAPI
from backend.routes import users, chatbot, appointments
from backend.database import create_tables

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])

@app.on_event("startup")
def startup():
    create_tables()

@app.get("/")
def root():
    return {"message": "Chatbot API is running!"}
