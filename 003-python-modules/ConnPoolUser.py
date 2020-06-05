import ConnPool
import mysql.connector
from mysql.connector import errors
import time

# fetch the second connection from the pool
db2 = mysql.connector.connect(pool_name='LoanDBConnPool')
print("Connection db2:", db2.connection_id)

# db2cur = db2.cursor()
# db2cur.execute("select sleep(10);")
# rows = db2cur.fetchall()
# db2cur.close()
# # db2.close()

# fetch the third connection from the pool
db3 = mysql.connector.connect(pool_name='LoanDBConnPool')
print("Connection db3:", db3.connection_id)    

def getConn():
    for i in range(5):
        
        if i == 4:
            db2.close()
            
        try:
            print("Attempt #",i)
            db4 = mysql.connector.connect(pool_name='LoanDBConnPool')
            print("Connection db4:", db4.connection_id)    
        except mysql.connector.errors.PoolError:
            print("Pool is maxed out")    
            time.sleep(3)
        else:
            break


"""
def runSQL():
    while True:
        try:
            conn = mysql.connector.connect(pool_name='LoanDBConnPool')
            cur = conn.cursor()
            cur.execute("select sleep(10);")
            rows = db2cur.fetchall()
            cur.close()
            conn.close()
        else:
            break
"""

