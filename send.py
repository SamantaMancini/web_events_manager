import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os




def send_mail(events):
    load_dotenv()
    # Email content
    content = events
    # Set up SMTP connection to Gmail's SMTP server
    try:
        mail = smtplib.SMTP(os.getenv('SMTP'), os.getenv('PORT'))
        # Identify yourself to the SMTP server
        mail.ehlo()  
        # Start TLS encryption for the connection
        mail.starttls()  
        # Gmail account credentials 
        sender = os.getenv('FROM')
        user = os.getenv('USER')
        password = os.getenv('PASSWORD')

        # Login to Gmail's SMTP server
        mail.login(user, password)

        # Email details
        recipient = os.getenv('RECIPIENT')
        subject = os.getenv('SUBJECT')

        # Construct email message with headers
        header = f'To: {recipient}\nFrom: {sender}\nSubject: {subject}\n'
        msg = MIMEText(content)
        msg['Subject'] = subject

        # Send email
        mail.sendmail(sender, recipient, msg.as_string())
        print("email mandata con successo")
        # Close SMTP connection
        mail.quit()
    except Exception as e:
        print(f"errore email {e}")

