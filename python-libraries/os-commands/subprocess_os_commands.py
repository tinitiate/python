# Python Execute OS Command with SubProcess Module

## Using subprocess.call
import subprocess

# Simple subprocess.call example
subprocess.call(['echo','Hello Tinitiate'], shell=True)

## Using subprocess.Popen
#* The **Popen** is similar to **call** except that it doestnt block, meaning,
#  it doesnt wait for the OS command to execute it will proceed with next 
#  steps in the python script.
#* To make the **subprocess.Popen** to wait we have to use `process.wait()` 
#  after the **subprocess.Popen**.
#* The **Popen** function can be used to capture the Standard Error 
#  and Standard output.
#* Here we demonstrate the following
#  * Code to capture standard Output from OS command
#  * Code to capture standard Error from OS command

# Capture Standard Output
# Execute a SYNTACTICALLY VALID DOS command on windows using subprocess.Popen
# Capture Standard Out and Standard Error in SDOut and SDErr variables
(standard_output,standard_error) = subprocess.Popen( ['echo','Hello World!']
                                 ,stdout=subprocess.PIPE
                                 ,stderr=subprocess.PIPE
                                 ,shell=True).communicate()

# Print the standard_output and standard_error variables
print(standard_output)
print(standard_error)

print("---------------")

# Capture Standard Error
# Execute a SYNTACTICALLY INVALID DOS command on windows using subprocess.Popen
# Intentionally Generate Error, and capture the error message to STDErr variable
(standard_output,standard_error) = subprocess.Popen( ['eco','Error']
                                 ,stdout=subprocess.PIPE
                                 ,stderr=subprocess.PIPE
                                 ,shell=True).communicate()
# Print the standard_output and standard_error variables
print(standard_output)
print(standard_error)

print("---------------")

# Execute a Python Script
(standard_output,standard_error) = subprocess.Popen( ['python','D:/training/PythonFeb2024/code/python-libraries/os-commands\\os_test.py']
                                 ,stdout=subprocess.PIPE
                                 ,stderr=subprocess.PIPE
                                 ,shell=True).communicate()

# Print the standard_output and standard_error variables
print(standard_output)
print(standard_error)
