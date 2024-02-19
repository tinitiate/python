import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import configparser
import os

# Load the configuration from file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the Gmail username and password from the configuration
gmail_user = config.get('Gmail', 'username')
gmail_password = config.get('Gmail', 'password')

# Create SENDER and RECEIVER
sender = 'tinitiate.training@gmail.com'
receiver = ['tinitiate@gmail.com', 'tinitiate.training@gmail.com']

# Create message object
msg = MIMEMultipart('alternative')
msg['From'] = sender 
msg['To'] = ", ".join(receiver)
msg['Subject'] = "This is a TINITIATE test EMAIL"

# Create the body of the message with plain-text and HTML
plain_text = "This is plain text"

# Create HTML text
html_text = """\
<html>
  <body>
    <h1>This is a TEST EMAIL FROM TINITIATE </h1>
    <p>
     Welcome to Python training from TINITATE.COM
    </p>
  </body>
</html>
"""

# CREATE MIME types for text/plain and text/html.
plain_message = MIMEText(plain_text, 'plain')
html_message = MIMEText(html_text, 'html')

# Attach them to the message
msg.attach(plain_message)
msg.attach(html_message)

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.ehlo()
s.login(gmail_user, gmail_password)

# sendmail function requires 3 arguments: sender, recipient and message
s.sendmail(sender, receiver, msg.as_string())

# Close SMTP connection once email is sent
s.quit()
