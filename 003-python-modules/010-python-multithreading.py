#========================================================================================
# TOPIC: PYTHON - MultiThreading Parallel programming Concurrent programming
#========================================================================================
# NOTES: * PYTHON supports Multithreading
#        * Normal execution of python, where each step in the code is executed one after 
#          another is run as a single THREAD. but in a multi-threaded application, code 
#          (or steps) can be run together with another in parallel (two or more steps at  
#          the same time) even though the code is written one after another.
#        * Such a requirement is very much needed in a variety of applications, such as 
#          games GUI applications, large volume data processing..
#        * To invoke multithreading features we need to use the threading module
#        * We simulate multithreading by running a function that takes 5 seconds 
#          to run (there is a SLEEP command) twice and make the TWO 5 seconds run in 
#          FIVE seconds instead of 10 Seconds
#        * Create Threads using "_thread" module
#        * Create Threads using "threading" module Thread class
#        * Dynamically Create Threads, With Named Thread-IDs
#
#
#========================================================================================
#
# FILE-NAME       : 028_mutlithreading_basics.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2016
#
# DESC            : Python Regular Expressions Patterns
#
#========================================================================================

# IMPORT the required modules
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


#############################################
# 1) Create THREADS using the _thread module
#############################################

# USING the _thread.start_new_thread
# This function accepts a FUNCTION-name and FUNCTION-Parameters
# as its parameters
# In this case we want to run the function: five_seconds_process
# and its SINGLE parameter.
# Also make sure to include a "COMMA" after the LAST PARAMETER that
# is being passed to the _thread.start_new_thread

print("Demonstration of THREADS using the _thread module's start_new_thread function")

# Run five_seconds_process function as a THREAD with a THREAD-ID 1
_thread.start_new_thread(five_seconds_process,(1,))


# Run five_seconds_process function as a THREAD with a THREAD-ID 2
_thread.start_new_thread(five_seconds_process,(2,))


# This is needed, because all the threads will exit, if the main program finishes
# in order to keep the program alive  we make the program execute for 5 seconds
# This infact is running 3 Threads ! (Including the time.sleep(5)  below.
time.sleep(5)

print("");


################################################
# 2) Create THREADS using the threading module
################################################
print("Demonstration of THREADS using the threading module's Thread CLASS")

#Import the threading module
from threading import Thread 

# * The Thread CLASS constructor accepts a function and 
#   its argument list as a tuple.
# * When the OBJECT.start() function is called, it runs
#   as a thread. 


# Create a Thread Object using the Thread class of the threading module
t1 = Thread(target=five_seconds_process, args=(1,))
t1.start()


# Create one more Thread Object using the Thread class of the threading module
t2 = Thread(target=five_seconds_process, args=(2,))
t2.start()


################################################
# 3) Create Dynamic THREADS
################################################
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



#========================================================================================
# END OF CODE
#========================================================================================
#TAGS: PYTHON - MultiThreading Parallel programming Concurrent programming
#      using python _thread module, start_new_thread example tutorial
#      using python threading module Thread Class
#========================================================================================
