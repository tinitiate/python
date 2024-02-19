
import datetime
from threading import Thread 

"""
c = 0
print("Seq Billion Counter Start", datetime.datetime.now())
for i in range(1000000000):
    c+=1
    
print(c)
print("Seq Billion Counter End", datetime.datetime.now())



"""
print("Parallel Billion Counter Start", datetime.datetime.now())

data = {}

def count_large_num(i_thread_id, i_st, i_end):

    c = 0
    for i in range(i_st, i_end+1):
        c+=1
    data[i_thread_id] = c

n=5
target = 1000000000
# Create a Threads List
threads = []
threshold = target/n

l_st = 0
l_ed = 0

# Create n Threads
for threadID in range(n):

    l_st = l_ed + 1
    l_ed = l_ed + threshold
    
    t = Thread(target=count_large_num, args=(threadID,int(l_st),int(l_ed), ))
    t.start()
    threads.append(t)

# join all threads
for t in threads:
    t.join()
    
print(data)
res = 0
for i in data.values():
   res += i

print(res)   
print("Parallel Billion Counter End", datetime.datetime.now())

