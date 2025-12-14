from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.patient_dashboard, name="patient_dashboard"),
    path("doctors/", views.doctors_list, name="doctors_list"),
    path("doctor/<int:doctor_id>/", views.doctor_availabilities, name="doctor_availabilities"),
    path("book/<int:slot_id>/", views.book_slot, name="book_slot"),
]
