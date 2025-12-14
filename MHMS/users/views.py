from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User
from doctors.models import Department


def doctor_signup(request):
    departments = Department.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        department_id = request.POST.get("department")

        if User.objects.filter(email=email).exists():
            return render(request, "auth/doctor_signup.html", {
                "departments": departments,
                "error": "Email already registered"
            })

        User.objects.create_user(
            name=name,
            email=email,
            password=password,
            role="doctor",
            department_id=department_id   # ✅ NO import issue
        )

        return redirect("doctor_login")

    return render(request, "auth/doctor_signup.html", {
        "departments": departments
    })

def doctor_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email=email, password=password)

        if user and user.role == "doctor":
            login(request, user)
            return redirect("doctor_dashboard")

        return render(request, "auth/doctor_login.html", {"error": "Invalid credentials"})

    return render(request, "auth/doctor_login.html")

def patient_signup(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(email=email).exists():
            return render(request, "auth/patient_signup.html", {"error": "Email already registered"})

        User.objects.create_user(
            name=name,
            email=email,
            password=password,
            role="patient"
        )
        return redirect("patient_login")

    return render(request, "auth/patient_signup.html")


# --------------------------------------
# PATIENT LOGIN
# --------------------------------------
def patient_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email=email, password=password)

        if user and user.role == "patient":
            login(request, user)
            return redirect("patient_dashboard")

        return render(request, "auth/patient_login.html", {"error": "Invalid credentials"})

    return render(request, "auth/patient_login.html")


