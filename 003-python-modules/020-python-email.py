#========================================================================================
# TOPIC: PYTHON - SENDING EMAIL
#========================================================================================
# NOTES: * Sending Email from PYTHON
#        
#========================================================================================
#
# FILE-NAME       : 035_python_email.py
# DEPENDANT-FILES : * PYTHON provides the smtplib module to send emails
#                   * Provisions to send email, emails with attachments and HTML emails 
#                   * Send email with attachments
#                   * Send list of files from python as email attachments 
#                   * All code tested for python 3.0
# 
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2014
#
# DESC            : PYTHON EMAIL
#
#========================================================================================


# IMPORT the MODULE smtplib, to send emails
import smtplib, os


# IMPORT other required modules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# For attachments
from email.mime.base import MIMEBase
from email import encoders


##########################################
# 1) SENDING PLAIN TEXT EMAIL FROM PYTHON
##########################################

# Create SENDER and RECEIVER
sender    = 'from@1some_domain.com'
receiver  = ['person_ONE@1some_domain.com', 'person_TWO@1some_domain.com']

# Create message object
msg = MIMEMultipart('alternative')

msg['From']    = sender 
msg['To']      = receiver 
msg['Subject'] = "This is a TINITIATE test EMAIL"

# Send the message via your local SMTP server.
s = smtplib.SMTP('localhost')

# sendmail function requires 3 arguments: sender, recipient and message
s.sendmail(sender, receiver, msg.as_string())

# Close SMTP connection once email is sent
s.quit()


######################################
# 2) SENDING HTML EMAIL FROM PYTHON
######################################

# Create SENDER and RECEIVER
html_sender    = 'from@1some_domain.com'
html_receiver  = ['person_ONE@1some_domain.com', 'person_TWO@1some_domain.com']

# Create message object
html_msg = MIMEMultipart('alternative')

html_msg['From']    = sender 
html_msg['To']      = receiver 
html_msg['Subject'] = "This is a TINITIATE test HTML EMAIL"

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
html_msg.attach(plain_message)
html_msg.attach(html_message)


# Send the message via your local SMTP server.
s = smtplib.SMTP('localhost')

# sendmail function requires 3 arguments: sender, recipient and message
s.sendmail(sender, receiver, html_msg.as_string())

# Close SMTP connection once email is sent
s.quit()


###########################################
# 3) SENDING EMAIL ATTACHMENTS FROM PYTHON
###########################################

# Create SENDER and RECEIVER
attachment_sender    = 'from@1some_domain.com'
attachment_receiver  = ['person_ONE@1some_domain.com', 'person_TWO@1some_domain.com']

# Create message object
attachment_msg = MIMEMultipart()

attachment_msg['From']    = attachment_sender
attachment_msg['To']      = attachment_receiver
attachment_msg['Subject'] = 'Python Attachment test email'

# Files LIST
files = ["c:\\tinitiate\\text1.txt","c:\\tinitiate\\image1.gif","c:\\tinitiate\\music1.mp3"]

for f in files:
  part = MIMEBase('application', "octet-stream")
  part.set_payload( open(f,"rb").read() )
  encoders.encode_base64(part)
  part.add_header('Content-Disposition','attachment; filename="{0}"'.format(os.path.basename(f)))
  attachment_msg.attach(part)

# Create an SMTP connection
smtp = smtplib.SMTP("localhost")
smtp.sendmail(attachment_sender, attachment_receiver, attachment_msg.as_string())
smtp.quit()

#========================================================================================
# END OF CODE
#========================================================================================
#TAGS: PYTHON - Sending EMAIL from PYTHON email
#
#========================================================================================
