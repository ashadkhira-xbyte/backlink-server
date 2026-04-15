import smtplib
from email.mime.text import MIMEText

TRACK_ID = "user_123"

html = f"""
<html>
  <body>
    <p>Hello, this is a test email</p>
    <img src="http://192.168.1.249:5000/track?id={TRACK_ID}" width="1" height="1" />
  </body>
</html>
"""

msg = MIMEText(html, "html")
msg["Subject"] = "Test Email"
msg["From"] = "ashad.khira@xbyte.io"
msg["To"] = "ashad.khira.xbyte@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("ashad.khira@xbyte.io", "pablodbekabhpzyi")
    server.send_message(msg)
