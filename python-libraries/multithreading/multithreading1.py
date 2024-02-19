from threading import Thread 
import time

# Create a FUNCTION that takes FIVE seconds to execute (This is a wait (sleep) command
# that pauses the program for FIVE seconds
def five_seconds_process(thread_id):
    print("ThreadID: ",thread_id," Started at: ", time.time())
    for c in range(5):
        print("thread_id: ", thread_id," Iteration Number ", c+1)
        time.sleep(1) # This causes the program to PAUSE for 1 Sec
    print("ThreadID: ",thread_id," Ended at: ", time.time())

"""
# Sequential Execution
# ####################
five_seconds_process(1)
five_seconds_process(2)
"""

"""
# Parallel Execution
# ####################
# Create 2 Threads
# Create a Thread Object using the Thread class of the threading module
t1 = Thread(target=five_seconds_process, args=(1,))
t1.start()

# Create one more Thread Object using the Thread class of the threading module
t2 = Thread(target=five_seconds_process, args=(2,))
t2.start()
"""


# Parallel Execution DYNAMIC THREAD COUNT
# #######################################
# Create a Threads List
threads = []
print("Start")

# Create 5 Threads
for threadID in range(5):
    t = Thread(target=five_seconds_process, args=(threadID+1, ))
    t.start()
    threads.append(t)

# print("End Before Join")

# Join all threads, It stops the main program from completing execution before all
# threads are done executing 
for e in threads:
    e.join()

print("End After Join")
