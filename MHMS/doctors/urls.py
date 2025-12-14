from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.doctor_dashboard, name="doctor_dashboard"),
    path("availability/add/", views.add_availability, name="add_availability"),
    path("availability/delete/<int:slot_id>/", views.delete_availability, name="delete_availability"),
]
