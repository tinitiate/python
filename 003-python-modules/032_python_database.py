#========================================================================================
# TOPIC: PYTHON - Database Programmings
#========================================================================================
# NOTES: * PYTHON provides mechanisms to connect to various databases
#          and perform database operations like Create, insert, select
#        * There are many Open and Commercial Database connectivity 
#          modules available for download.
#        * In this program, we test with pyodbc an OpenSource PYTHON database 
#          connectivity module, And the cx_oracle module to connect to Oracle Database
#        * Almost all popular databases have Modules to connect to python.
#        * cx_Oracle module, This is a 3rd party module that needs to be downloaded 
#          separately to avoid errors like: "ImportError: DLL load failed: %1 is not a 
#		   valid Win32 application."
#        * Make sure the Oracle Client / Python and the cx_Oracle module are of the same 
#          bit version 32 all or 64 all, this is very important for this to work.          
#
#========================================================================================
#
# FILE-NAME       : 032_python_database.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2014
#
# DESC            : PYTHON Database Programming
#
#========================================================================================

#################################################
# 1) Connecting to Oracle Using cx_oracle module  
#################################################
import cx_Oracle


# Create a connection object, usage string
# USER/PASSWORD@INSTANCE-NAME-AS-IS-IN-TNSNAMES.ORA
connection = cx_Oracle.connect('BNCOM_STG/BNCOM_STG111@eordhistd')


# prints Oracle Version Details
print(connection.version)

# prints Current Schema name
print(connection.username)
# Note there are also startup/shutdown commands supported by cx_oracle


# Executing DDL (Data Definition Language)

# Create a table
cursor = connection.cursor()

print("Create a table ti_test, with multiple datatypes")
# python cx_oracle Create a table with multiple data types
cursor.execute("create table ti_test(col1 int,col2 varchar2(100),col3 date,col4 clob )" )


# python cx_oracle Alter Table using cx_python, to add primary key
print("Alter table ti_test, add primary key")
cursor.execute("alter table ti_test add constraint ti_test_pk primary key (col1)") 


# python cx_oracle Insert data into the table
cursor.execute("insert into ti_test values(1,'Test1',sysdate,'THIS IS CLOB DATA .....')")
cursor.execute("insert into ti_test values(2,'Test2',sysdate,'THIS IS CLOB DATA .....')")


# python cx_oracle Update data in the table
cursor.execute("update ti_test set col2 = 'DATA CHANGE' where col1 = 1")


# python cx_oracle delete data in the table
cursor.execute("delete ti_test where col1 = 2")


# Commit changes
connection.commit()


# Reading data from Oracle using cx_Oracle
# reading multiple datatypes and print to screen
cursor.execute("SELECT col1, col2, col3, col4 FROM ti_test")


# use fetchall() to get the list of row data
for l_col1, l_col2, l_col3, l_col4 in cursor.fetchall():
    print("l_col1: ", l_col1) 
    print("l_col2: ", l_col2)
    print("l_col3: ", l_col3)
    print("l_col4: ", l_col4)


# Drop table after test
print("drop table ti_test")
cursor.execute("drop table ti_test")


# Close the cursor object
cursor.close()


# Close the connection once completed
connection.close()

#========================================================================================
# END OF CODE
#========================================================================================
#TAGS: PYTHON - Connect to database programming insert select oracle create table python
#      python oracle cx_oracle pyodbc
#
#=======================================================================================
