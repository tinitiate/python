""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Modules Threading
MetaDescription: Python Modules, Threading, _thread
MetaKeywords: Python Modules, Threading, _thread
Author: Venkata Bhattaram / tinitiate.com
ContentName: python-modules-threading
---
MARKDOWN """

""" MARKDOWN
# PYTHON MULTITHREADING PARALLEL / CONCURRENT PROGRAMMING
* PYTHON supports Multithreading
* Normal execution of python, where each step in the code is executed one after 
  another is run as a single THREAD. but in a multi-threaded application, code 
  (or steps) can be run together with another in parallel (two or more steps at  
  the same time) even though the code is written one after another.
* Such a requirement is very much needed in a variety of applications, such as 
  games, GUI applications, large volume data processing.
* To invoke multithreading features we need to use the threading module
* Here we demonstrate multithreading by
  * Running a function that takes 5 seconds to complete execution using a SLEEP 
    command.
  * We run the function TWICE and it takes 10 Secs to complete the execution in 
    sequential execution.
  * But when we run the same function in TWO threads parallelly then it takes 
    only 5 secs to run both the functions at the same time concurrently.
MARKDOWN """

    
""" MARKDOWN
# CREATE THREADS USING THE _THREAD MODULE
* USING the _thread.start_new_thread we can pass any function and its parameters
  that we want to run as a parallel thread.
* This function accepts TWO parameters (1) Target function (2) List of function 
  parameters
* In this case we want to run the function: five_seconds_process
  and its SINGLE parameter.  Also make sure to include a "COMMA" after the 
  LAST PARAMETER that is being passed to the _thread.start_new_thread
MARKDOWN """

# MARKDOWN ```
import _thread
import time

# Create a FUNCTION that takes FIVE seconds to execute (This is a wait (sleep) command
# that pauses the program for FIVE seconds
def five_seconds_process(thread_id):
    "This function when called takes 5 Seconds to execute"
    # Thread Start message
    print("ThreadID: ",thread_id," Started at: ", time.time())
    for c in range(5):
        print("thread_id: ", thread_id," Iteration Number ", c+1)
        time.sleep(1) # This causes the program to PAUSE for 1 Sec
    # Thread END message
    print("ThreadID: ",thread_id," Ended at: ", time.time())
# ----


print("Demonstration of THREADS using the _thread module's start_new_thread function")

# Run five_seconds_process function as a THREAD with a THREAD-ID 1
_thread.start_new_thread(five_seconds_process,(1,))


# Run five_seconds_process function as a THREAD with a THREAD-ID 2
_thread.start_new_thread(five_seconds_process,(2,))


# This is needed, because all the threads will exit, if the main program finishes
# in order to keep the program alive  we make the program execute for 5 seconds
# This infact is running 3 Threads ! (Including the time.sleep(5)  below.
time.sleep(5)
# MARKDOWN ```


""" MARKDOWN
# CREATE THREADS USING THE THREADING MODULE
* The **Thread** class from the **threading** module is another and preferred 
  way to create threads.
* The Thread CLASS constructor accepts a function and its argument list as 
  a tuple.
* When the OBJECT.start() function is called, it runs as a thread. 
MARKDOWN """
# MARKDOWN ```

#Import the threading module
from threading import Thread 

# Create a FUNCTION that takes FIVE seconds to execute (This is a wait (sleep) command
# that pauses the program for FIVE seconds
def five_seconds_process(thread_id):
    "This function when called takes 5 Seconds to execute"
    # Thread Start message
    print("ThreadID: ",thread_id," Started at: ", time.time())
    for c in range(5):
        print("thread_id: ", thread_id," Iteration Number ", c+1)
        time.sleep(1) # This causes the program to PAUSE for 1 Sec
    # Thread END message
    print("ThreadID: ",thread_id," Ended at: ", time.time())


# Create a Thread Object using the Thread class of the threading module
t1 = Thread(target=five_seconds_process, args=(1,))
t1.start()


# Create one more Thread Object using the Thread class of the threading module
t2 = Thread(target=five_seconds_process, args=(2,))
t2.start()
# MARKDOWN ```


""" MARKDOWN
# CREATE DYNAMIC NUMBER THREADS
* Sometimes the number of threads that are needed might depend on volume of 
  process, for such scenarios we can dynamically create threads, using a loop.
* Here we demonstrate creating THREE threads using a for loop and run the same 
  function five_seconds_process THRICE using a thread each.
MARKDOWN """
# MARKDOWN ```
from threading import Thread 

# Create a FUNCTION that takes FIVE seconds to execute (This is a wait (sleep) command
# that pauses the program for FIVE seconds
def five_seconds_process(thread_id):
    "This function when called takes 5 Seconds to execute"
    # Thread Start message
    print("ThreadID: ",thread_id," Started at: ", time.time())
    for c in range(5):
        print("thread_id: ", thread_id," Iteration Number ", c+1)
        time.sleep(1) # This causes the program to PAUSE for 1 Sec
    # Thread END message
    print("ThreadID: ",thread_id," Ended at: ", time.time())

# Create a Threads List
threads = []

# Create 3 Threads
for threadID in range(2):
    t = Thread(target=five_seconds_process, args=(threadID+1, ))
    t.start()
    # threads.append(t)

# join all threads
for t in threads:
    t.join()
# MARKDOWN ```
