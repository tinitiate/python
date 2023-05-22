import pymssql

conn = pymssql.connect(server="127.0.0.1", port="1433", user="sa", password="tinitiate_01", database="tinitiate")
cursor = conn.cursor()

cursor.execute('select * FROM employees.emp;')
data=cursor.fetchall()
print(data)
