# alert_system.py - Sends alerts via email/Slack/Discord
import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    sender_email = "your_email@example.com"
    receiver_email = "soc_team@example.com"
    msg = MIMEText(message)
    msg['Subject'] = "Dark Web Threat Alert"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login(sender_email, "your_password")
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Alert sent successfully!")
    except Exception as e:
        print(f"Failed to send alert: {e}")

if __name__ == "__main__":
    send_alert("New dark web exploit detected!")
