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