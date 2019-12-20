#========================================================================================
# TOPIC: PYTHON - SENDING EMAIL
#========================================================================================
# NOTES: * PYTHON provides a standard logging module to log messages
#        * LOG to Console
#        * LOG to File
#        
#========================================================================================
#
# FILE-NAME       : 036_python_logger.py
# DEPENDANT-FILES : N/A 
# 
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2014
#
# DESC            : PYTHON LOGGING
#
#========================================================================================

import sys, logging

##########################
# 1) LOG to CONSOLE
##########################

# Create a LOGGING Object
tinitiateLOG = logging.getLogger('tinitiate')
tinitiateLOG.setLevel(logging.DEBUG)
print(tinitiateLOG.getEffectiveLevel())


# Create a Streamhandler for console
tinLOG = logging.StreamHandler( sys.__stdout__ )


# Print to console level, Add the stream handler to Console
tinLOG.setLevel(logging.DEBUG)
tinitiateLOG.addHandler(tinLOG)


# Use the functions [debug, info, warn, error] of the logging object
tinitiateLOG.debug('This is a debug message')
tinitiateLOG.info('This is a info message')
tinitiateLOG.warn('This is a warning message')
tinitiateLOG.error('This is an error message')
tinitiateLOG.critical('This is a critical message')

##########################
# 2) LOG to FILE
##########################

# Create a File Handler
LogFile = logging.FileHandler('c:\\tinitiate\\tinPython.log')

# Set Log level of ERROR, ONLY ERROR or HIGHER are logged to FILE
LogFile.setLevel(logging.ERROR)

# Add the handler to the logging object
tinitiateLOG.addHandler(LogFile)

# Run Log messages
tinitiateLOG.debug('This is a debug message')
tinitiateLOG.info('This is a info message')
tinitiateLOG.warn('This is a warning message')

# ONLY THE FOLLOEING MESSAGES ARE LOGGED TO FILE
tinitiateLOG.error('This is an error message')
tinitiateLOG.critical('This is a critical message')


#========================================================================================
# END OF CODE
#========================================================================================
#TAGS: PYTHON - LOGGING  LOG DEBUG LOG ERROR LOG WARNING LOG ERROR LOG CRITICAL
#               LOG TO CONSOLE LOG TO FILE
#========================================================================================
