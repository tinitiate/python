
# Empty List
emp = []
print(emp)


emp1 = {"EmpID":1,"Ename":"AAA","Sal":2000,"projects":[11,22]}
emp2 = {"EmpID":2,"Ename":"BBB","Sal":4000,"projects":[1,22]}
emp3 = {"EmpID":3,"Ename":"CCC","Sal":5000,"projects":[1,552]}
print(emp1["Sal"])

emp.append(emp1)
emp.append(emp2)
emp.append(emp3)
print(emp)

print(emp[0]["Sal"])
print(emp[2]["projects"][1]+1)

print(emp[1])
print(emp[1]["Sal"])
print(emp[2]["projects"][1])
