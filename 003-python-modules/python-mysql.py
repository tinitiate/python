import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='tinitiate', db='mysql')

# Clear Contents

# Create A Data Base
# Executing DDL (Data Definition Language)

# Create a table
cursor = conn.cursor()

try:
    cursor.execute("drop table ti_test");
except:
    pass;


# Python pymysql MYSQL Create a table with multiple data types
cursor.execute(" create table ti_test ( col1 int, col2 varchar(100), col3 date, col4 text );" )


# python pymysql MYSQL Alter Table to add primary key
cursor.execute("alter table ti_test add constraint ti_test_pk primary key (col1);")


# Python pymysql MYSQL Insert data into the table
cursor.execute("insert into ti_test values (1, 'Test', curdate(), 'THIS IS CLOB DATA .........');")
cursor.execute("insert into ti_test values (2, 'Test2', curdate(), 'THIS IS CLOB DATA .........');")


# python pymysql MYSQL Update data in the table
cursor.execute("update ti_test set col2 = 'DATA CHANGE' where col1 = 1;")


# python pymysql MYSQL delete data in the table
cursor.execute("delete from ti_test where col1 = 2;")


# Commit changes
conn.commit()


cursor.execute("insert into ti_test values (3, 'Test3', curdate(), '333 THIS IS CLOB DATA .........');")
cursor.execute("insert into ti_test values (4, 'Test4', curdate(), '444 THIS IS CLOB DATA .........');")
cursor.execute("insert into ti_test values (5, 'Test5', curdate(), '555 THIS IS CLOB DATA .........');")

cursor.execute("select col1,col2,col3,col4 from ti_test;")
# Fetches a Single Row
rowdata = cursor.fetchone()
print(rowdata)


# reading multiple datatypes and print to screen
# use fetchall() to get the list of row data
for l_col1, l_col2, l_col3, l_col4 in cursor.fetchall():
    print("l_col1: ", l_col1)
    print("l_col2: ", l_col2)
    print("l_col3: ", l_col3)
    print("l_col4: ", l_col4)

# To RollBack changes
conn.rollback()

cursor.execute("select col1,col2,col3,col4 from ti_test;")
    
# Prints the Row count of the cursor
print(cursor.rowcount)

# Fetches a Single Row
rowdata = cursor.fetchone()
print(rowdata)

# use fetchall() to get the list of row data
for l_col1, l_col2, l_col3, l_col4 in cursor.fetchall():
    print("l_col1: ", l_col1)
    print("l_col2: ", l_col2)
    print("l_col3: ", l_col3)
    print("l_col4: ", l_col4)


# Drop table after test
print("drop table ti_test")
cursor.execute("drop table ti_test")


# Close the Cursor
cursor.close()

# Close the Connection
conn.close()
