# Mini-Hospital-Management-System
A role-based **Mini Hospital Management System** built with **Django** and an integrated **Serverless Email Notification Service** using **AWS Lambda (Serverless Framework)**.

This project demonstrates real-world backend concepts such as:

* Custom authentication
* Role-based access (Doctor & Patient)
* Appointment booking system
* Department-based doctor discovery
  
---
## 📌 Features

### 👨‍⚕️ Doctor

* Signup & Login
* Select **Department** during signup
* Doctor Dashboard
* Add / Manage availability time slots
* View:

  * Upcoming booked appointments
  * Past unbooked (unused) slots

### 🧑‍⚕️ Patient

* Signup & Login
* Patient Dashboard
* View doctors **with department names**
* View available time slots
* Book one appointment slot
* Slot becomes unavailable immediately after booking

  * `SIGNUP_WELCOME`
  * `BOOKING_CONFIRMATION`
---

## 🛠️ Tech Stack

| Layer      | Technology                |
| ---------- | ------------------------- |
| Backend    | Django (Python)           |
| Auth       | Custom User Model         |
| Database   | SQLite (Dev)              |
---

## 📂 Project Structure

```
MHMS/
│
├── users/          # Custom user model, auth (Doctor / Patient)
├── doctors/        # Departments, availability, doctor dashboard
├── patients/       # Patient dashboard & booking logic
├── templates/      # HTML templates
├── utils/          # Email service caller
├── manage.py
└── db.sqlite3
├── requirements.txt
```

---

## ⚙️ Installation (MHMS Backend)

### 1️⃣ Clone Repository

```bash
git clone <repo-url>
cd MHMS
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install django requests
```

### 4️⃣ Configure Settings

In `settings.py`:

```python
AUTH_USER_MODEL = "users.User"
```

Ensure templates directory is added:

```python
"DIRS": [BASE_DIR / "templates"],
```

### 5️⃣ Migrate Database

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6️⃣ Add Departments

Via Admin Panel:

```
http://127.0.0.1:8000/admin/
```

Add examples:

* Cardiology
* Orthopedics
* Pediatrics

### 7️⃣ Run Server

```bash
python manage.py runserver
```

## 🔐 Roles & Access Control

* Doctors can only manage **their own slots**
* Patients can only book **available slots**
* Role-based redirects after login

---

## ✅ Business Rules Implemented

* One slot → one booking only
* Booked slot disappears from availability
* Past booked appointments are removed
* Past unbooked slots remain visible to doctor

---

## 🚀 Future Enhancements

* Filter doctors by department (patient side)
* Appointment cancellation
* Appointment history
* Email reminders
* Google Calendar integration
* AWS SES for production email

---

## 👨‍💻 Author

**Mini Hospital Management System (MHMS)**
Built for learning, evaluation & real-world backend practice.

---

## 📜 License

This project is for educational purposes.
