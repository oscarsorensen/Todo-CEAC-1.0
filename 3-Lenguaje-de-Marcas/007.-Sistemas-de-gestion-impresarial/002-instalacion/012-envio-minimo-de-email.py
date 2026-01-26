import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

msg = EmailMessage()
msg["From"] = SMTP_USER
msg["To"] = SMTP_USER
msg["Subject"] = "Esto es un ejercicio de clase. With better safety"
msg.set_content("Hola esto es una prueba desde Python.\n")

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASS)
    smtp.send_message(msg)

print("Email sent")

