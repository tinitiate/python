---
YamlDesc: CONTENT-ARTICLE
Title: Python Execute OS Commands
MetaDescription: Python Execute OS Commands,subprocess example code, tutorials
MetaKeywords: python functions, function with parameters, function with return value example code, tutorials
Author: Sravya Myla
ContentName: os-commands
---

# Python Execute OS Command
* Python provides ways to execute OS commands
* Using "OS" Module "system" function
* Using the "subprocess.call"

## OS Module
### Using os.system 
# Executing OS command using the OS Module  
```python
import os
# String to store the OS command
OScommand = "echo Tinitiate.com"

# Run the OS command using system function
os.system(OScommand)

# OUTPUT: Tinitiate.com
```


## SubProcess Module
### Using subprocess.call
* 
```python
# Executing OS command SubProcess Module
import subprocess
subprocess.call(['echo','Hello Tinitiate'], shell=True)

# OUTPUT: 
```

### Using subprocess.Popen
* The **Popen** is similar to **call** except that it doestnt block, meaning,
  it doesnt wait for the OS command to execute it will proceed with next 
  steps in the python script.
* To make the **subprocess.Popen** to wait we have to use `process.wait()` 
  after the **subprocess.Popen**.
* The **Popen** function can be used to capture the Standard Error 
  and Standard output.
* Here we demonstrate the following
  * Code to capture standard Output from OS command
  * Code to capture standard Error from OS command


```python
# Capture Standard Output
# Execute a SYNTACTICALLY VALID DOS command on windows using subprocess.Popen
# Capture Standard Out and Standard Error in SDOut and SDErr variables
import subprocess
(SDOut,SDErr) = subprocess.Popen( ['echo','Hello World!']
                                 ,stdout=subprocess.PIPE
                                 ,stderr=subprocess.PIPE
                                 ,shell=True).communicate()

# Print the SDOut and SDErr variables
print(SDOut)
print(SDErr)

# OUTPUT: b'\n'
#b''


# Capture Standard Error
# Execute a SYNTACTICALLY INVALID DOS command on windows using subprocess.Popen
# Intentionally Generate Error, and capture the error message to STDErr variable
import subprocess

(SDOut,SDErr) = subprocess.Popen( ['cat','Hello World!.txt']
                                 ,stdout=subprocess.PIPE
                                 ,stderr=subprocess.PIPE
                                 ,shell=True).communicate()


# Use wait for the OS command to execute, using wait
process = subprocess.Popen( ['echo','Hello World!']
                             ,stdout=subprocess.PIPE
                             ,stderr=subprocess.PIPE
                             ,shell=True).communicate()
process.wait()

```
