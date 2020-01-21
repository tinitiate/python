## >---
## >YamlDesc: CONTENT-ARTICLE
## >Title: python variables
## >MetaDescription: python print statement, c style print, string.format, Print UNICODE, ASCII raw tutorials example code, tutorials
## >MetaKeywords: python print statement, c style print, string.format, Print UNICODE, ASCII raw tutorials example code, tutorials
## >Author: Venkata Bhattaram / tinitiate.com
## >ContentName: variables-operators
## >---

## >## Python Variables
## >* Variables are memory locations that are assigned by the python interpreter 
## >* In python, There is no specific variable declaration and variable
## >  initialization.
## >* Python supports variable creation and initialization in one go
## >```
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

# Deleting  a single object or multiple objects by using the del statement.
# For example:
del variable1;
# using the variable after deleting the object will raise an error
# the below statement will raise an error
# print("variable1 reassigned value: ", variable1);

# More syntax variations for creating variables 
var1 = var2 = 100;
print("var1 : ", var1);
print("var2 : ", var2);

var100, var200 = 100, 200;
print("var100 : ", var100);
print("var200 : ", var200);
## >```


## >## Python Operators
## >* Mathematical Operators
## >* Augmented assignment Operators
## >```
# Test Variables
A = 1
B = 2
C = 3

# Sum, Difference, product, divide, mod, power
# Add, subtract, multiply 
print(A+B+C) # OUTPUT: 6
print(A-B)   # OUTPUT: -1
print(100/3) # OUTPUT: 33.333333333333336

# remainder, mod
print(100%3) # OUTPUT: 1

# power, exponential operator
print(4**2)  # OUTPUT: 16

# Augmented assign
A += 4   # A=A+4
print(A) # OUTPUT: 5  

B *= 4   # B=B*4
print(B) # OUTPUT: 8

# For strings
S="-hello-"
S *= 3
print(S) # OUTPUT: -hello--hello--hello-
## >```
