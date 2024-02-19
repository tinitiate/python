emp = []

# print(emp)

emp1 = {"EmpID":1,"Ename":"AAA","Sal":5000,"projects":[11,22]}
emp2 = {"EmpID":2,"Ename":"BBB","Sal":43000,"projects":[1,22]}
emp3 = {"EmpID":3,"Ename":"CCC","Sal":2000,"projects":[1,552]}
emp4 = {"EmpID":4,"Ename":"DDD","Sal":43000,"projects":[1,999]}
emp5 = {"EmpID":5,"Ename":"EEE","Sal":43000,"projects":[1,999]}

emp.append(emp1)
emp.append(emp2)
emp.append(emp3)
emp.append(emp4)
emp.append(emp5)
# print(emp)

# Print the name of employees working in Project 1
for e in emp: # Loop
    for project in e["projects"]:
        if project == 1:
            print(e["Ename"])


"""
# Print the name of emp(s) who makes the highest sal
highest_sal = 0
emp_name = []
ctr = 1
for e in emp: # Loop
    # Condition 1
    # Execute only ONCE for the entire loop
    if ctr == 1:
        highest_sal = e["Sal"]
        ctr = 2

    # Condition 2    
    # Check if the current iteration sal is < highest_sal variable
    # ONLY then update the highest_sal variable
    if e["Sal"] > highest_sal:
        highest_sal = e["Sal"]
        emp_name.clear()
        emp_name.append(e["Ename"])
    elif e["Sal"] == highest_sal:
        emp_name.append(e["Ename"])


print(emp_name)
print(highest_sal)
"""

"""
# Print the name of emp who makes the lowest sal
lowest_sal = 0
emp_name = ""
ctr = 1
for e in emp: # Loop
    # Condition 1
    # Execute only ONCE for the entire loop
    if ctr == 1:
        lowest_sal = e["Sal"]
        ctr = 2

    # Condition 2    
    # Check if the current iteration sal is < lowest_sal variable
    # ONLY then update the lowest_sal variable
    if e["Sal"] < lowest_sal:
        lowest_sal = e["Sal"]
        emp_name = e["Ename"]

print(emp_name)
print(lowest_sal)
"""

"""
# Print 999
for e in emp: # Loop
    # print(e)  # Iteration
    if e["EmpID"] == 4:
        print(e["projects"][1])
"""
"""
# Get me the emps whose sal > 2000
for e in emp: # Loop
    if e["Sal"] > 2000:
        print(e["Ename"])
"""

# print the name of emp who makes the highest sal
"""
# Prints only the first HIT of max sal
max_sal = -1
max_sal_ename = ""
for employee in emp:
    # print(employee)
    if employee["Sal"] > max_sal:
        max_sal = employee["Sal"]
        max_sal_ename = employee["Ename"]
print(max_sal_ename)

max_sal_list = []
max_sal = -1
max_sal_ename = ""
for employee in emp:
    # print(employee)
    if employee["Sal"] > max_sal:
        max_sal = employee["Sal"]
        max_sal_list = []
        max_sal_list.append(employee["Ename"])
    elif employee["Sal"] == max_sal:
        max_sal_list.append(employee["Ename"])

print(max_sal_list)

# print the name of emp who are working in project 22

# Method - 1
for employee in emp:
    # print(employee)
    if 22 in employee["projects"]:
        print(employee["Ename"])

# Method - 2
for employee in emp:
    # print(employee)
    for project in employee["projects"]:
        if project == 22:
            print(employee["Ename"])
"""

"""
# print the name of emp whose sal = 4000
for employee in emp:
    print(employee)
    if employee["Sal"]==5000:
        print(employee["Ename"])
"""
