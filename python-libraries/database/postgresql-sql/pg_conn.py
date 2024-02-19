import psycopg2

# Create Connection Object
# ##############################################################################
conn = psycopg2.connect(database="postgres"
                       ,user = "tinitiate"
                       ,password = "Tinitiate!23456"
                       ,host = "127.0.0.1" # localhost
                       ,port = "5432")

cursor = conn.cursor()

"""
# Executing DDL (Data Definition Language)
# ##############################################################################

# Try to Drop the table
cursor.execute('set search_path="public"')

try:
    cursor.execute("drop table ti_test");
except:
    pass


# Python pymysql MYSQL Create a table with multiple data types
cursor.execute("create table ti_test ( col1 int, col2 varchar(100), col3 date, col4 text )" )

# python pymysql MYSQL Alter Table to add primary key
cursor.execute("alter table ti_test add constraint ti_test_pk primary key (col1)")


# Executing DML (Data Manipulation Language)
# ##############################################################################

# Python pymysql MYSQL Insert data into the table
cursor.execute("insert into ti_test values (1, 'Test', now(), 'THIS IS CLOB DATA .........');")
cursor.execute("insert into ti_test values (2, 'Test2', now(), 'THIS IS CLOB DATA .........');")


# python pymysql MYSQL Update data in the table
cursor.execute("update ti_test set col2 = '1DATA CHANGE' where col1 = 1;")


# python pymysql MYSQL delete data in the table
cursor.execute("delete from ti_test where col1 = 2;")

cursor.execute("insert into ti_test values (3, 'T1est3', now(), '333 THIS IS CLOB DATA .........');")
cursor.execute("insert into ti_test values (4, 'T1est4', now(), '444 THIS IS CLOB DATA .........');")

conn.commit()

cursor.execute("insert into ti_test values (5, 'T1est5', now(), '555 THIS IS CLOB DATA .........');")


# To RollBack changes
conn.rollback()

"""
# Executing Data Selection
# ##############################################################################

# Fetch One Row
cursor.execute("select col1,col2,col3,col4 from ti_test;")

# Prints the Row count of the cursor
print(cursor.rowcount)

# Fetches a Single Row
rowdata = cursor.fetchone()
print(rowdata)


# Reading multiple datatypes and print to screen
cursor.execute("select col1,col2,col3,col4 from ti_test;")
# use fetchall() to get the list of row data
for l_col1, l_col2, l_col3, l_col4 in cursor.fetchall():
    print("l_col1: ", l_col1)
    print("l_col2: ", l_col2)
    print("l_col3: ", l_col3)
    print("l_col4: ", l_col4)


# Close the Cursor
cursor.close()

# Close the Connection
conn.close()