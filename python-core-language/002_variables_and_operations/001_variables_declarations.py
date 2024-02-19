# Simple variable creation
variable1 = 1;          # Integer
variable2 = "test";     # String
variable3 = 100.4;      # double value

# Print all the three variables 
print("variable1 : ", variable1);
print("variable2 : ", variable2);
print("variable3 : ", variable3);

# reassign a value to a variable
variable1 = 4;          # Integer
print("variable1 reassigned value: ", variable1);

variable1 = variable2
# 1 = 5
# 'aa' = 'bbb'

# Deleting  a single object or multiple objects by using the del statement.
# For example:
del variable1;
# using the variable after deleting the object will raise an error
# the below statement will raise an error
#print("variable1 reassigned value: ", variable1);

# More syntax variations for creating variables 
var1 = var2 = 100;
print("var1 : ", var1);
print("var2 : ", var2);

var100, var200 = 100, 200;
print("var100 : ", var100);
print("var200 : ", var200);