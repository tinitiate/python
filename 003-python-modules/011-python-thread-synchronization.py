#========================================================================================
# TOPIC: PYTHON - MultiThreading Parallel programming Concurrent programming
#========================================================================================
# NOTES: * This program demonstrates the PYTHON thread synchronization mechanisms 
#          (this is about Thread conflict and deadlock resolution)
#        * THREAD CONTENTION: two processes trying to use the same resource 
#		   at the same time        
#        * Threads might share the same resource and in such cases there could be 
#          various contention issues (who should use the resource first.)
#        * A resource here could be anything from a variable to a file or any thing that 
#          must be used sequentially.
#        * LOCKS: One solution to overcome this issue is using LOCKS.
#        * Python Locks supports locked and unlocked states, a lock will have EXCLUSIVE 
#          access to the shared resource during the lock period, 
#		   this will prevent contention 
#        * lock can be acquired using the "acquire()" function and unlock can be issued 
#          using release() function.
#        * PYTHON semaphores, acquire() semaphore.release()
#        * SEMAPHORES are one more mechanism to implement synchronization,
#        * They have an internal counter which starts to decrement when an acquire() call  
#          is made and starts to increment when a release() call is made. The counter  
#          will never go below zero; but when it is zero, it blocks, waiting for a thread  
#		   to call the release()
#        * They are very useful to manage Database connection pools, File writing 
#          services and situations where precaution needs to be taken when the shared 
#          resource has limited capacity. 

#========================================================================================
#
# FILE-NAME       : 030_thread_synchronization.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2014
#
# DESC            : Python Multithreading: thread synchronization 
#                   (Thread conflict and deadlock resolution)
#
#========================================================================================

########################################
# 1) PYTHON THREAD Contention Scenario
########################################

# Create a SHARED resource a "print to screen" method 
# Required for SLEEP operation
from threading import Thread, Lock, RLock, Semaphore
import time


print("CONTENTION SCENARIO")
print("Thread UnSafe execution where there is no Order of printing messages")
print("--------------------------------------------------------------------")


# * This is a class [commonResource] a function prints a message  
#   to SCREEN three times,waiting a second in-between the PRINT.
# * We run the CLASS-Function three times in THREE Threads.
# * The output is not consistant and  overlaps
# * This is because the common resource (the Print3Times function)
#   is not locked or synchronized 

class commonResource:
    "this is a class that provides a file and file writing function"
    def Print3Times(self, message):
        for c in range(3):
            print(message)
            time.sleep(1) # This causes the program to PAUSE for 1 Sec

# End of Class


# Create 3 Objects for the class
# each object will run the same function as a single thread
ObjRunner =  commonResource();


# We have 3 messages to print one for each thread
AAA_message="A"
BBB_message="B"
CCC_message="C"


# start the Thread to write to file
t1 = Thread( target=ObjRunner.Print3Times
            ,args=(AAA_message,))

t2 = Thread( target=ObjRunner.Print3Times
            ,args=(BBB_message,))

t3 = Thread( target=ObjRunner.Print3Times
            ,args=(CCC_message,))


# Start each of the thread
t1.start()
t2.start()
t3.start()

# Wait for the threads to complete
t1.join()
t2.join()
t3.join()

# Note that the OutPut is not in order and is inconsistant, as the same print statement 
# is being used by all the threads


print("NON-CONTENTION SCENARIO, Using LOCKS")
print("Thread Safe execution where there is the specified Order of printing messages")
print("-----------------------------------------------------------------------------")



# To over come this issue we have to SYNCHRONIZE the process.

#####################################
# 2) Using Locks to avoid contention
#####################################
# Using the lock mechanism to implement synchronization
# re-writing the same above program with locking using acquire() and release()


class ThreadSafeCommonResource:
    "this is a class that provides a file and file writing function"


 # The FUNCTION Print2Console to make is synchronized, must accept a LOCK TYPE parameters
    def Print2Console(self, message, lock):

        # CREATE A LOCK, Using the lock object 
        # (this is a common object across all the threads)
        lock.acquire()

        # Do the Processing
        for c in range(3):
            time.sleep(1) # This causes the program to PAUSE for 1 Sec
            print(message)

        # RELEASE the LOCK, Using the lock object 
        # (this is a common object across all the threads)
        lock.release()

# End of Class

# Create a common LOCK object for all the threads


# Create ONE Objects for the class
# The same object will run as 3 threads
ts_ObjRunner =  ThreadSafeCommonResource()

lock = Lock()

# start the Thread to write to file
t1 = Thread( target=ts_ObjRunner.Print2Console, args=[AAA_message, lock,])
t2 = Thread( target=ts_ObjRunner.Print2Console, args=[BBB_message, lock,])
t3 = Thread( target=ts_ObjRunner.Print2Console, args=[CCC_message, lock,])


# Start each of the thread
t1.start()
t2.start()
t3.start()

# Wait for the threads to complete
t1.join()
t2.join()
t3.join()


# Here using the LOCK, the output is consistant and as expected
# there is no contention, but the flipside is the performance is lowered 
# on using the LOCK synchronization.



print("NON-CONTENTION SCENARIO, Using SEMAPHORES")
print("Thread Safe execution where there is the specified Order of printing messages")
print("-----------------------------------------------------------------------------")


####################################
# 3) SEMAPHORES
####################################
# * SEMAPHORES are one more mechanism to implement synchronization,
# * They have an internal counter which starts to decrement when an acquire() call is  
#   made and starts to increment when a release() call is made. The counter will never go 
#   below zero; but when it is zero, it blocks, waiting for a thread to call the release()
# * They are very useful to manage Database connection pools, File writing services
#   and situations where precaution needs to be taken when the shared resource has
#   limited capacity. 


# The below function implements the use of semaphores
def Print2ConsoleSemaphore(message, semaphore):

    # CREATE A semaphore, Using the semaphore object 
    # (this is a common object across all the threads)
    semaphore.acquire()

    # Do the Processing
    for c in range(3):
        time.sleep(1) # This causes the program to PAUSE for 1 Sec
        print(message)

    # RELEASE the semaphore, Using the semaphore object 
    # (this is a common object across all the threads)
    semaphore.release()


#Run the above function in Three threads

semaphore = Semaphore()

# start the Thread to write to file
t1 = Thread( target=Print2ConsoleSemaphore, args=[AAA_message, semaphore,])
t2 = Thread( target=Print2ConsoleSemaphore, args=[BBB_message, semaphore,])
t3 = Thread( target=Print2ConsoleSemaphore, args=[CCC_message, semaphore,])


# Start each of the thread
t1.start()
t2.start()
t3.start()

# Wait for the threads to complete
t1.join()
t2.join()
t3.join()


#========================================================================================
# END OF CODE
#========================================================================================
#TAGS: PYTHON - thread synchronization Locks RLocks Semaphores Conditions
#
#========================================================================================
