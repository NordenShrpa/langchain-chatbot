from datetime import datetime
import re
from backend.services.user_service import validate_email, validate_phone
from backend.services.date_parser import extract_date  # Correct module for extract_date

appointments = []

def validate_date(input_text):
    """Parses date (e.g., 'Next Monday' → YYYY-MM-DD)."""
    if input_text.lower() == "next monday":
        next_monday = datetime.today().strftime('%Y-%m-%d')
        return next_monday
    return input_text  

def book_appointment(user_id: str, user_input: str):
    """Books an appointment after validation."""
    appointment_date = extract_date(user_input)  
    if not appointment_date:
        return "Could not extract a valid date from your input."
    
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    if not re.match(date_pattern, appointment_date):
        return "Invalid date format. Please provide YYYY-MM-DD."

    new_appointment = {"user_id": user_id, "appointment_date": appointment_date}
    appointments.append(new_appointment)
    return f"Appointment booked for {appointment_date}."

def get_appointments():
    """Retrieves all booked appointments."""
    return appointments
