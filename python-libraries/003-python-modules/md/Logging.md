# Logging 

- The logging module is part of Python's standard library and provides a flexible way to log messages from your application.
- The module provides different logging levels:
  - DEBUG
  - INFO
  - WARNING
  - ERROR
  - CRITICAL.
- The logging module can write logs to various destinations, including a file, the console, email, and more.
- The module provides different loggers that can be used to categorize logs based on their source, like a specific module or subsystem.
- It is possible to configure the logging module to include additional information like the time of the log message, the process ID, or the thread ID.
- The logging module provides a powerful filter mechanism that can be used to control which log messages are written to a destination based on various criteria.
- The module can be customized with formatters to control the appearance of the log messages. A formatter can be used to specify the message format, the date format, or to include additional contextual information.
- The logging module can be used with try-except blocks to catch and log exceptions that occur in your application.
- The logging module supports logging in a distributed environment, where logs are collected and aggregated from multiple sources, such as different nodes or containers.

##  Log to Console 

```python
import sys, logging

# Create a LOGGING Object
tiConsLog = logging.getLogger('tinitiate-console')

# Create a Streamhandler for the LOGGING Object
ConsHandler = logging.StreamHandler( sys.__stdout__ )

# Set Log Formatting
formatter = logging.Formatter('[%(asctime)s] %(name)-12s: %(levelname)-8s %(message)s')
ConsHandler.setFormatter(formatter)

# Add the Console Handler to the LOGGING Object
tiConsLog.addHandler(ConsHandler)

# Set Log Level
tiConsLog.setLevel(logging.DEBUG)
# print(tiConsLog.getEffectiveLevel())


# Use the functions [debug, info, warn, error] of the logging object
tiConsLog.debug('This is a debug message')
tiConsLog.info('This is a info message')
tiConsLog.warning('This is a warning message')
tiConsLog.error('This is an error message')
tiConsLog.critical('This is a critical message')

# Change Log level and retry logging all level log messages
tiConsLog.setLevel(logging.ERROR)

tiConsLog.debug('This is a debug message')
tiConsLog.info('This is a info message')
tiConsLog.warning('This is a warning message')
tiConsLog.error('This is an error message')
tiConsLog.critical('This is a critical message')

```

## Log to File 

```python
import sys, logging

# Create a LOGGING Object
tiFileLog = logging.getLogger('tinitiate-file')

# Create a Log File Handler, the log messages will be created in this file
LogFile = logging.FileHandler('E:\\python-master\\media\\tinPython.log')

# Set Log Formatting
formatter = logging.Formatter('[%(asctime)s] %(name)-12s: %(levelname)-8s %(message)s')
LogFile.setFormatter(formatter)

# Add the handler to the logging object
tiFileLog.addHandler(LogFile)

# Set Log Level
tiFileLog.setLevel(logging.ERROR)


# Run Log messages
tiFileLog.debug('This is a debug message')
tiFileLog.info('This is a info message')
tiFileLog.warning('This is a warning message')

# ONLY THE FOLLOEING MESSAGES ARE LOGGED TO FILE
tiFileLog.error('This is an error message')
tiFileLog.critical('This is a critical message')

```

## Log to Email 

```python
import logging
import smtplib
from logging.handlers import SMTPHandler

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Set up email handler
smtp_handler = SMTPHandler(
    mailhost='smtp.example.com',
    fromaddr='sender@example.com',
    toaddrs=['recipient@example.com'],
    subject='Error occurred!',
    credentials=('username', 'password'),
    secure=(),
)
smtp_handler.setLevel(logging.ERROR)
logger.addHandler(smtp_handler)

# Test the logger
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

```

