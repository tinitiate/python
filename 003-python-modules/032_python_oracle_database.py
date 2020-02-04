""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: python oracle database
MetaDescription: python Connect to oracle database, CRUD, insert, update, select, oracle, create  example code, tutorials
MetaKeywords: python oracle database example code, tutorials
Author: Venkata Bhattaram / tinitiate.com
ContentName: python-oracle-database
---
MARKDOWN """

""" MARKDOWN
# Python cx_Oracle Oracle Database Programming
* PYTHON provides mechanisms to connect to various databases
  and perform database operations like Create, insert, select
* There are many Open and Commercial Database connectivity
  modules available for download.
* In this program, we test with cx_Oracle an OpenSource PYTHON database
  connectivity module, And the cx_oracle module is used to connect to Oracle Database
* cx_oracle also supports startup/shutdown commands.
* cx_Oracle module, This is a 3rd party module that needs to be downloaded
  separately to avoid errors like: "ImportError: DLL load failed: %1 is not a
  Valid Win32 application."
* Make sure the Oracle Client / Python and the cx_Oracle module are of the same
  bit version 32 all or 64 all, this is very important for this to work.
MARKDOWN """

"""
set PATH=%PATH%;C:\Personal\instantclient_12_2\
set ORACLE_HOME=C:\Personal\instantclient_12_2\

import os  
os.environ["PATH"] += os.pathsep + os.pathsep.join(["C:\\Personal\\instantclient_12_2\\"])
os.environ["ORACLE_HOME"] = "C:\\Personal\\instantclient_12_2\\"
"""

# MARKDOWN ```

# Connecting to Oracle Using cx_oracle module
import cx_Oracle

# Create Connection Object
# ##############################################################################
# Create a connection object, usage string
# USER/PASSWORD@INSTANCE-NAME-AS-IS-IN-TNSNAMES.ORA
connection = cx_Oracle.connect('tinitiate/tinitiate@my_database')
cursor = connection.cursor()

# prints Oracle Version Details
print(connection.version)
# prints Current Schema name
print(connection.username)


# Executing DDL (Data Definition Language)
# ##############################################################################
# Try to Drop the table
try:
    cursor.execute("drop table ti_test");
except:
    pass;
    
# python cx_oracle Create a table with multiple data types
cursor.execute("create table ti_test(col1 int,col2 varchar2(100),col3 date,col4 clob )" )

# python cx_oracle Alter Table using cx_python, to add primary key
cursor.execute("alter table ti_test add constraint ti_test_pk primary key (col1)")


# Executing DML (Data Manipulation Language)
# ##############################################################################
# python cx_oracle Insert data into the table
cursor.execute("insert into ti_test values(1,'Test1',sysdate,'THIS IS CLOB DATA .....')")
cursor.execute("insert into ti_test values(2,'Test2',sysdate,'THIS IS CLOB DATA .....')")

# python cx_oracle Update data in the table
cursor.execute("update ti_test set col2 = 'DATA CHANGE' where col1 = 1")

# python cx_oracle delete data in the table
cursor.execute("delete ti_test where col1 = 2")

cursor.execute("insert into ti_test values(3,'Test3',sysdate,'THIS IS CLOB DATA .....')")
cursor.execute("insert into ti_test values(4,'Test4',sysdate,'THIS IS CLOB DATA .....')")

# Commit changes
connection.commit()

# Insert one more row
cursor.execute("insert into ti_test values(5,'Test5',sysdate,'THIS IS CLOB DATA .....')")

# To RollBack changes
conn.rollback()


# Executing Data Selection
# ##############################################################################

# Fetch One Row
cursor.execute("select col1,col2,col3,col4 from ti_test;")

# Prints the Row count of the cursor
print(cursor.rowcount)

# Fetches a Single Row
rowdata = cursor.fetchone()
print(rowdata)

# Reading data from Oracle using cx_Oracle
cursor.execute("SELECT col1, col2, col3, col4 FROM ti_test")

# use fetchall() to get the list of row data
for l_col1, l_col2, l_col3, l_col4 in cursor.fetchall():
    print("l_col1: ", l_col1)
    print("l_col2: ", l_col2)
    print("l_col3: ", l_col3)
    print("l_col4: ", l_col4)


# Close the cursor object
cursor.close()

# Close the connection once completed
connection.close()

# MARKDOWN ```
