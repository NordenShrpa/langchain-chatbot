from googleapiclient.discovery import build
from google.oauth2 import service_account
import os

SCOPES = ["https://www.googleapis.com/auth/calendar"]
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_CREDENTIALS_JSON")

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build("calendar", "v3", credentials=credentials)

def create_event(summary: str, start_time: str, end_time: str):
    event = {
        "summary": summary,
        "start": {"dateTime": start_time, "timeZone": "UTC"},
        "end": {"dateTime": end_time, "timeZone": "UTC"},
    }
    event = service.events().insert(calendarId="primary", body=event).execute()
    return event.get("htmlLink")

def schedule_event(summary: str, start_time: str, end_time: str):
    """Schedules an event in Google Calendar."""
    return create_event(summary, start_time, end_time)