import sys, logging
import time
# Create a LOGGING Object
tiFileLog = logging.getLogger('tinitiate-file')

l_log_file_name = "app_log"+ str(time.time()) + ".log"

# Create a Log File Handler, the log messages will be created in this file
LogFile = logging.FileHandler('D:/training/PythonFeb2024/'+ l_log_file_name)

# Set Log Formatting
formatter = logging.Formatter('[%(asctime)s] %(name)-12s: %(levelname)-8s %(message)s')
LogFile.setFormatter(formatter)

# Add the handler to the logging object
tiFileLog.addHandler(LogFile)

# Set Log Level
tiFileLog.setLevel(logging.DEBUG)

# Run Log messages
tiFileLog.debug('This is a debug message')
tiFileLog.info('This is a info message')
tiFileLog.warning('This is a warning message')

# ONLY THE FOLLOWING MESSAGES ARE LOGGED TO FILE
tiFileLog.error('This is an error message')
tiFileLog.critical('This is a critical message')

# Functionl Coding with Logger
# ##############################################
def add2nums(n1,n2,log_obj):
    try:
        log_obj.debug('Functional Inputs: n1 = ' + str(n1) + " || n2 = " + str(n2))
        print(n1+n2)
    except Exception as e:
        log_obj.error('Functional Inputs: n1 = ' + str(n1) + " || n2 = " + str(n2))
        log_obj.error(str(type(e).__name__) +" "+ str(e))
        

tiFileLog.debug('Starting Adder')
add2nums(12,22,tiFileLog)         # pass logger object as parameter
add2nums('a',22,tiFileLog)

# OOP Coding with Logger
# ##############################################
class math1():

    def __init__(self,p_log_obj):
        # Instance Variable
        self.log_obj = p_log_obj
        self.log_obj.setLevel(logging.ERROR)

    def add2nums(self,n1,n2):
        try:
            self.log_obj.debug('OOP Inputs: n1 = ' + str(n1) + " || n2 = " + str(n2))
            print(n1+n2)
        except Exception as e:
            self.log_obj.error('OOP Inputs: n1 = ' + str(n1) + " || n2 = " + str(n2))
            self.log_obj.error(str(type(e).__name__) +" "+ str(e))

a1 = math1(tiFileLog)   # pass logger object in cons
a1.add2nums(22, 11)
a1.add2nums(22, 'bbb')
