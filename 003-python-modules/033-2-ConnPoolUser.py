""" MARKDOWN
---
Title: python mysql connection pool caller
Keywords: python mysql connection pool caller
Author: Venkata Bhattaram
---
MARKDOWN """

""" MARKDOWN
# Python Connection Pool caller for MySQL
* This program uses the connection pool.
MARKDOWN """

# MARKDOWN ```
import ConnPool
import mysql.connector
from mysql.connector import errors
import time

# Open Two Connections
##########################################################
db2 = mysql.connector.connect(pool_name='LoanDBConnPool')
print("Connection db2:", db2.connection_id)


# fetch the third connection from the pool
db3 = mysql.connector.connect(pool_name='LoanDBConnPool')
print("Connection db3:", db3.connection_id)    


# This function closes and uses the existing connections
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


# Run the Get Conn function to use connection pool by closing some 
# existing connections.
getConn()

# MARKDOWN ```
