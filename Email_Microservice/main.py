import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from email_utils import send_email
import os

PORT = int(os.getenv("Email_Service_PORT", 8001))
app = FastAPI()
app = FastAPI()


class EmailRequest(BaseModel):
    action: str
    to_email: str
    data: dict


@app.post("/send-email")
def send_email_api(request: EmailRequest):
    try:
        if request.action == "SIGNUP_WELCOME":
            subject = "Welcome to MHMS"
            message = f"""
Hello {request.data.get('name')},

Welcome to Mini Hospital Management System (MHMS).
Your account has been created successfully.

Regards,
MHMS Team
"""

        elif request.action == "BOOKING_CONFIRMATION":
            subject = "MHMS Appointment Confirmation"
            message = f"""
Hello {request.data.get('patient_name')},

Your appointment has been confirmed.

Doctor: Dr. {request.data.get('doctor_name')}
Date: {request.data.get('date')}
Time: {request.data.get('time')}

Regards,
MHMS Team
"""
        elif request.action == "DOCTOR_BOOKING_NOTIFICATION":
            subject = "New Appointment Booked"
            message = f"""
Hello Dr. {request.data.get('doctor_name')},

A new appointment has been booked.

Patient: {request.data.get('patient_name')}
Date: {request.data.get('date')}
Time: {request.data.get('time')}

Please log in to your dashboard for details.

Regards,
MHMS Team
"""

        else:
            raise HTTPException(status_code=400, detail="Invalid action")

        send_email(request.to_email, subject, message)
        return {"status": "success", "message": "Email sent"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
