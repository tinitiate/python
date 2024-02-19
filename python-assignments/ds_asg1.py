
emps = []
print(emps)

emp1 = {"empid":1,"ename":"aa","sal":2000}
emp2 = {"empid":2,"ename":"bb","sal":2300}
emp3 = {"empid":3,"ename":"cc","sal":3000}
emp4 = {"ename":"dd","sal":3500,"empid":4}

emps.append(emp1)
emps.append(emp2)
emps.append(emp3)

print(emps)
print(emps[1])
emps[0]["projects"]=[11,22,33]
emps[1]["projects"]=[22,33,55]
emps[2]["projects"]=[33]
print(emps)
print(emps[1]["projects"][2])
print(emps[1]["projects"])
print(emps[1]["sal"])
emps[1]["sal"] = emps[1]["sal"] + 100
"""
print(emps[1]["sal"]+100)
print(emps)
"""

# {'empid': 2, 'ename': 'bb', 'sal': 2300, 'projects': [22, 33, 55]}