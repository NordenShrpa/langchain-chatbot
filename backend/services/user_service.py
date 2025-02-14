import re

def validate_email(email: str) -> bool:
    """Validates the email format."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_phone(phone: str) -> bool:
    """Validates the phone number format."""
    phone_regex = r'^\+?[1-9]\d{1,14}$'  
    return re.match(phone_regex, phone) is not None

def collect_user_info(name: str, email: str, phone: str):
    """Collects and validates user information."""
    if not validate_email(email):
        return "Invalid email format."
    if not validate_phone(phone):
        return "Invalid phone number format."
    return "User information collected successfully."
