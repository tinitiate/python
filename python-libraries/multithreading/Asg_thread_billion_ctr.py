import datetime
from threading import Thread 

"""
# Sequential Billion Counter
# ##################################################
today = datetime.datetime.today()
print("Start",today.strftime("%d-%b-%Y %H:%M:%S"))

a = 0
for c in range(1,1000000001):
    a = a+1

print(a)

today = datetime.datetime.today()
print("End",today.strftime("%d-%b-%Y %H:%M:%S"))
# Stats
# ###########################
# Start 05-Oct-2023 18:13:42
# 1000000000
# End 05-Oct-2023 18:15:00
"""


# Parallel Billion Counter
# ##################################################
today = datetime.datetime.today()
print("Start",today.strftime("%d-%b-%Y %H:%M:%S"))

l_thread_stats = {}
# {1:250000000,2:250000000,3:250000000,4:250000000}
def counter_vals(p_start,p_end,p_thread):
    a = 0
    for c1 in range(p_start,p_end+1):
        a = a+1

    l_thread_stats[p_thread] = a 

# counter_vals(1,250000000,1)
# counter_vals(250000001,500000000,2)
# counter_vals(500000001,750000000,3)
# counter_vals(750000001,1000000000,4)

t1 = Thread(target=counter_vals, args=(1,250000000,1))
t1.start()
t2 = Thread(target=counter_vals, args=(250000001,500000000,2))
t2.start()
t3 = Thread(target=counter_vals, args=(500000001,750000000,3))
t3.start()
t4 = Thread(target=counter_vals, args=(750000001,1000000000,4))
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

ctr = 0
# l_thread_stats = {1:250000000,2:250000000,3:250000000,4:250000000}
for k,v in l_thread_stats.items():
    ctr = ctr + v

print(ctr)

today = datetime.datetime.today()
print("End",today.strftime("%d-%b-%Y %H:%M:%S"))

# Start 05-Oct-2023 18:27:04
# 1000000000
# End 05-Oct-2023 18:27:47
