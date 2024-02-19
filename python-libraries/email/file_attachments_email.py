import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import configparser
import os

data_dir ='E:/python-master/media/003-python-modules/'
# Load the configuration from file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the Gmail username and password from the configuration
gmail_user = config.get('Gmail', 'username')
gmail_password = config.get('Gmail', 'password')

# Create SENDER and RECEIVER
attachment_sender = 'tinitiate.training@gmail.com'
attachment_receiver = ['tinitiate@gmail.com', 'tinitiate.training@gmail.com']

# Create message object
attachment_msg = MIMEMultipart()

attachment_msg['From']    = attachment_sender
attachment_msg['To']      =  ", ".join(attachment_receiver)
attachment_msg['Subject'] = 'Python Attachment test email'

# Files LIST
files = [data_dir+"myfile.txt",data_dir+"image1.gif",data_dir+"music1.mp3"]

for f in files:
  part = MIMEBase('application', "octet-stream")
  part.set_payload( open(f,"rb").read() )
  encoders.encode_base64(part)
  part.add_header('Content-Disposition','attachment; filename="{0}"'.format(os.path.basename(f)))
  attachment_msg.attach(part)

# Create an SMTP connection
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login(gmail_user, gmail_password)
s.ehlo()
s.sendmail(attachment_sender, attachment_receiver, attachment_msg.as_string())
s.quit()




