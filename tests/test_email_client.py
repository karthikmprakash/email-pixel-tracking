import os
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app"))
)
from config import settings


def send_test_email():
    sender_email = settings.smtp_email
    receiver_email = settings.receiver_email
    subject = "Test Email with Tracking Pixel"
    tracking_pixel_url = f"{settings.server_url}/track/{receiver_email}"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    html = f"""
    <html>
    <body>
        <p>This is a test email with a tracking pixel.</p>
        <img src="{tracking_pixel_url}" alt="tracking pixel" style="display:none;">
    </body>
    </html>
    """

    part = MIMEText(html, "html")
    msg.attach(part)

    with smtplib.SMTP(settings.smtp_server, 587) as server:
        server.starttls()
        server.login(sender_email, settings.smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    send_test_email()
