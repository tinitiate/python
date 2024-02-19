# IMPORT the MODULE smtplib, to send emails
import smtplib, os

# IMPORT other required modules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# For attachments
from email.mime.base import MIMEBase
from email import encoders

# For congigurations
import configparser
import os

# Load the configuration from file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the Gmail username and password from the configuration
gmail_user = config.get('Gmail', 'username')
gmail_password = config.get('Gmail', 'password')

##########################################
# 1) SENDING PLAIN TEXT EMAIL FROM PYTHON
##########################################

# Create SENDER and RECEIVER
sender    = 'tinitiate.training@gmail.com'
receiver  = ['tinitiate@gmail.com', 'tinitiate.training@gmail.com']


# Create message object
msg = MIMEMultipart('alternative')

msg['From']    = sender 
# msg['To']      = receiver 
msg['To'] = ", ".join(receiver)
msg['Subject'] = "This is a TINITIATE test EMAIL"

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.ehlo()
s.login(gmail_user, gmail_password)


# sendmail function requires 3 arguments: sender, recipient and message
s.sendmail(sender, receiver, msg.as_string())

# Close SMTP connection once email is sent
s.quit()


