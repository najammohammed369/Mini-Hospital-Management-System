import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ===== SMTP CONFIG =====
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "najam.mohammed369@gmail.com"          # 🔴 change
SENDER_PASSWORD = "fiux vuvu boby ekpg"         # 🔴 change


def send_email(to_email, subject, message):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    server.quit()
