# Subprocess Wait
# The wait() method in the subprocess.Popen class waits for the process to 
# complete and returns the exit code.
# process using Popen, the process runs asynchronously in the background.
# wait() allows your code to wait until the process finishes before proceeding.
# This is useful when you need to ensure that a process has completed before
# continuing with the rest of your code.
# In the following example, process.wait() is called after communicate(),
# which means the code will wait for the echo command to finish executing
# before moving on to the next line of code.
import subprocess

process = subprocess.Popen(['echo', 'Hello World!'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           shell=True)
output, error = process.communicate()
process.wait()
