from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from doctors.models import Availability
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings


# --------------------------------------
# PATIENT DASHBOARD
# --------------------------------------
def patient_dashboard(request):
    return render(request, "patient/dashboard.html")


# --------------------------------------
# SHOW ALL DOCTORS
# --------------------------------------
def doctors_list(request):
    doctors = User.objects.filter(role="doctor")
    return render(request, "patient/doctors_list.html", {"doctors": doctors})


# --------------------------------------
# SHOW DOCTOR'S AVAILABLE SLOTS
# --------------------------------------
def doctor_availabilities(request, doctor_id):
    doctor = get_object_or_404(User, id=doctor_id, role="doctor")

    # Only show available (not booked) slots
    slots = Availability.objects.filter(doctor=doctor, is_booked=False)

    return render(request, "patient/doctor_availabilities.html", {
        "doctor": doctor,
        "slots": slots
    })


# --------------------------------------
# BOOK A SLOT
# --------------------------------------
def book_slot(request, slot_id):
    slot = get_object_or_404(Availability, id=slot_id)

    if slot.is_booked:
        messages.error(request, "Slot already booked!")
        return redirect("patient_dashboard")

    # Mark slot as booked
    slot.is_booked = True
    slot.save()

    messages.success(request, "Your appointment is booked successfully!")
    return redirect("patient_dashboard")


def send_appointment_email(patient_email, doctor_name, date, time):
    subject = "Appointment Confirmation"
    message = f"Your appointment with Dr. {doctor_name} is confirmed for {date} at {time}."

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [patient_email],
        fail_silently=False,
    )
