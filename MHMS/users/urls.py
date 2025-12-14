from django.urls import path
from . import views

urlpatterns = [
    path("doctor/signup/", views.doctor_signup, name="doctor_signup"),
    path("doctor/login/", views.doctor_login, name="doctor_login"),
    path("patient/signup/", views.patient_signup, name="patient_signup"),
    path("patient/login/", views.patient_login, name="patient_login"),
]
