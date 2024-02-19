# Read nested elements from List of Dictionaries
list_dict = [{'EmpID':1, 'EmpName':'Venkat'},
             {'EmpID':2, 'EmpName':'Sujatha'},
             {'EmpID':3, 'EmpName':'Taran'}]


# Print Name of EmpID: 3
# EmpID: 3 is 3rd element, whose index is "2"
print(list_dict[2]['EmpName'])