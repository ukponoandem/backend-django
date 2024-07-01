import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, from_email, password):
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to Outlook's SMTP server
        server = smtplib.SMTP("smtp-mail.outlook.com", 587)
        server.starttls()  # Start TLS encryption
        server.login(from_email, password)  # Login to your account

        # Send email
        server.sendmail(from_email, to_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        # Close the connection
        server.quit()
