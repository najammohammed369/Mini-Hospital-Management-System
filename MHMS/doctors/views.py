from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import datetime
from users.decorators import doctor_required
from .models import Availability

@doctor_required
def doctor_dashboard(request):
    now = timezone.now()

    slots = Availability.objects.filter(doctor=request.user)

    upcoming_slots =[]
    upcoming_booked = []
    past_unbooked = []

    for slot in slots:
        slot_end_datetime = datetime.combine(slot.date, slot.end_time)
        slot_end_datetime = timezone.make_aware(slot_end_datetime)

        # PAST  → DELETE
        if slot_end_datetime < now and slot.is_booked:
            slot.delete()
            continue

        # FUTURE + BOOKED → UPCOMING APPOINTMENT
        if slot_end_datetime >= now and slot.is_booked:
            upcoming_booked.append(slot)

        # PAST + UNBOOKED → SHOW AS UNUSED
        if slot_end_datetime < now and not slot.is_booked:
            past_unbooked.append(slot)

        # FUTURE + UNBOOKED -> SHOW AS UPCOMING APPOINTMENT
        if slot_end_datetime >= now and not slot.is_booked:
            upcoming_slots.append(slot)

    return render(request, "doctors/dashboard.html", {
        "upcoming_slots": upcoming_slots,
        "upcoming_appointments": upcoming_booked,
        "past_unbooked_slots": past_unbooked,
    })

@doctor_required
def add_availability(request):
    if request.method == "POST":
        Availability.objects.create(
            doctor=request.user,
            date=request.POST["date"],
            start_time=request.POST["start_time"],
            end_time=request.POST["end_time"]
        )
        return redirect("doctor_dashboard")

    return render(request, "doctors/add_availability.html")



@doctor_required
def delete_availability(request, slot_id):
    slot = get_object_or_404(Availability, id=slot_id)

    # Ensure doctor owns this slot
    if slot.doctor != request.user:
        return redirect("doctor_dashboard")

    slot.delete()
    return redirect("doctor_dashboard")