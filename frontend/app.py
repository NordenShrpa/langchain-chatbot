import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Backend URLs
CHATBOT_URL = "http://localhost:8000/chat"
BOOK_APPOINTMENT_URL = "http://localhost:8000/book/"
VIEW_APPOINTMENTS_URL = "http://localhost:8000/appointments"

# Function to interact with chatbot
def chat_with_bot(user_query):
    try:
        response = requests.post(CHATBOT_URL, json={"query": user_query})
        response.raise_for_status()
        return response.json().get("response", "No response from the chatbot")
    except requests.exceptions.RequestException as e:
        return f"Error connecting to chatbot: {e}"

# Function to book an appointment
def book_appointment(user_input):
    try:
        response = requests.post(BOOK_APPOINTMENT_URL, json={"user_id": "123", "user_input": user_input})
        response.raise_for_status()
        return response.json().get("message", "Error booking appointment")
    except requests.exceptions.RequestException as e:
        return f"Error connecting to appointment system: {e}"

# Function to view appointments
def get_appointments():
    try:
        response = requests.get(VIEW_APPOINTMENTS_URL)
        response.raise_for_status()
        return response.json().get("appointments", [])
    except requests.exceptions.RequestException as e:
        return f"Error fetching appointments: {e}"

# Streamlit UI
st.title("🤖 AI Chatbot with Document Search & Appointment Booking")

# Chatbot interaction
user_input = st.text_input("Ask me anything:")
if st.button("Send"):
    response = chat_with_bot(user_input)
    st.write("🤖 Chatbot:", response)

# Appointment booking
st.subheader("📅 Book an Appointment")
appointment_input = st.text_input("Enter date (e.g., Next Monday):")
if st.button("Book Appointment"):
    booking_response = book_appointment(appointment_input)
    st.write("✅", booking_response)

# View appointments
st.subheader("📂 View Appointments")
if st.button("Show Appointments"):
    appointments = get_appointments()
    if isinstance(appointments, list):
        for appointment in appointments:
            st.write("📅", appointment.get("appointment_date", "Unknown date"))
    else:
        st.write("⚠️", appointments)

