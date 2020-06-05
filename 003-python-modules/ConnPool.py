# pip install mysql-connector-python-rf
import mysql.connector
from mysql.connector import errors
 
# create connection pool and fetch the first connection
db1 = mysql.connector.connect( user='root'
                              ,password='tinitiate'
                              ,host='127.0.0.1'
                              ,database='testing'
                              ,pool_name='LoanDBConnPool'
                              ,pool_size=3)
                              
print("Mother Connection:", db1.connection_id)

# The getConn makes 5 Attempts, with a wait time of 2 Secs between each attempt
def getConn():
    for i in range(5):
        try:
            print("Attempt #",i)
            db4 = mysql.connector.connect(pool_name='LoanDBConnPool')
            print("Connection db4:", db4.connection_id)
            return db4
        except mysql.connector.errors.PoolError:
            time.sleep(2)

    return("Pool is maxed out")
