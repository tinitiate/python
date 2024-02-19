emps = []
print(emps)

emp1 = {"empid":1,"ename":"aa","sal":2000,"projects":[22],"details":{"duration":24,"credits":10}}
emp2 = {"empid":2,"ename":"bb","sal":2300,"projects":[44],"details":{"duration":24,"credits":50}}
emp3 = {"empid":3,"ename":"cc","sal":3000,"projects":[22,33],"details":{"duration":24,"credits":30}}
emp4 = {"ename":"dd","sal":3500,"empid":4,"projects":[22,44],"details":{"duration":24,"credits":50}}
emp5 = {"empid":5,"ename":"ee","sal":100,"projects":[22,33],"details":{"duration":24,"credits":100}}
emp6 = {"ename":"ff","sal":3500,"empid":6,"projects":[22,44],"details":{"duration":24,"credits":100}}

emps.append(emp1)
emps.append(emp2)
emps.append(emp3)
emps.append(emp4)
emps.append(emp5)
emps.append(emp6)
# emps.append(22)
print(emps)

# Print the name of emp who makes the highest sal
#
max_sal = 0
max_sal_ename = ""
# 
for emp in emps:
    # print(emp["sal"])
    if max_sal < emp["sal"]:
        max_sal = emp["sal"]
        max_sal_ename = emp["ename"]

print("Highest Sal Maker", max_sal_ename)


# Print the name of emp who works in project 22 and has the highest credits
#

"""
# Print Name of Emp whose sal is > 2000
#
for emp in emps:
    # print(emp)
    if emp["sal"] > 2000:
        print(emp["ename"])

print("========")
# Print Name of Emp whose works for project 44 and sal is >= 3000
#
for emp in emps:
    # print(emp)
    if emp["sal"] >= 3000 and 44 in emp["projects"]:
        print(emp["ename"])


for emp in emps:
    # print(emp)
    if emp["sal"] >= 3000:
        for project in emp["projects"]:
            if project == 44:
                print(emp["ename"])

# {"ename":"dd","sal":3500,"empid":4,"projects":[22,44]}            

"""