import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_test_email():
    sender_email = "karthik@akaiketech.com"
    receiver_email = "mkarthikprakash.work@gmail.com"
    subject = "Test Email with Tracking Pixel"
    tracking_pixel_url = f"http://127.0.0.1:8000/track/{receiver_email}"

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

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("karthik@akaiketech.com", "imflrelwzlzsadzp")
        server.sendmail(
            "karthik@akaiketech.com", "mkarthikprakash.work@gmail.com", msg.as_string()
        )


if __name__ == "__main__":
    send_test_email()
