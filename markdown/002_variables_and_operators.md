---
YamlDesc: CONTENT-ARTICLE
Title: python variables
MetaDescription: python print statement, c style print, string.format, Print UNICODE, ASCII raw tutorials example code, tutorials
MetaKeywords: python print statement, c style print, string.format, Print UNICODE, ASCII raw tutorials example code, tutorials
Author: Sravya Myla
ContentName: variables-operators
---

## Python Variables
* Variables are memory locations that are assigned by the python interpreter 
* In python, There is no specific variable declaration and variable
  initialization.
* Python supports variable creation and initialization in one go

```python
# Simple variable creation
variable1 = 1;          # Integer
variable2 = "test";     # String
variable3 = 100.4;      # double value

# Print all the three variables 
print("variable1 : ", variable1);
print("variable2 : ", variable2);
print("variable3 : ", variable3);

# OUTPUT: variable1 :  1
variable2 :  test
variable3 :  100.4
```

```python
# reassign a value to a variable
# Simple variable creation
variable1 = 1;          # Integer
variable2 = "test";     # String
variable3 = 100.4;      # double value
variable1 = 4;          # Integer
print("variable1 reassigned value: ", variable1);

# OUTPUT: variable1 reassigned value:  4
```

```python
# Deleting  a single object or multiple objects by using the del statement.
# For example:
variable1 = 1;          # Integer
variable2 = "test";     # String
variable3 = 100.4;      # double value
del variable1;
print (variable1)

# OUTPUT: NameError: name 'variable1' is not defined.
```
```python
# using the variable after deleting the object will raise an error
# the below statement will raise an error
variable1 = 1;          # Integer
print("variable1 reassigned value: ", variable1);

# OUTPUT: variable1 reassigned value:  1
```

```python
# More syntax variations for creating variables 
var1 = var2 = 100;
print("var1 : ", var1);
print("var2 : ", var2);

var100, var200 = 100, 200;
print("var100 : ", var100);
print("var200 : ", var200);

# OUTPUT: var1 :  100
var2 :  100
var100 :  100
var200 :  200
```
## Python Operators
* Mathematical Operators
* Augmented assignment Operators
```python
# Test Variables
A = 1
B = 2
C = 3

# Sum, Difference, product, divide, mod, power
# Add, subtract, multiply 
print(A+B+C) 
# OUTPUT: 6
print(A-B)   
# OUTPUT: -1
print(100/3)

# OUTPUT: 33.333333333333336
```

```python
# remainder, mod
# Test Variables
A = 1
B = 2
C = 3
print(100%3) 

# OUTPUT: 1
```

```python
# power, exponential operator
# Test Variables
A = 1
B = 2
C = 3
print(4**2)  

# OUTPUT: 16
```

```python
# Augmented assign
# Test Variables
A = 1
B = 2
C = 3
A += 4   # A=A+4
print(A) 

# OUTPUT: 5  
```

```python
# Test Variables
A = 1
B = 2
C = 3
B *= 4   # B=B*4
print(B)

# OUTPUT: 8
```

```python
# For strings
# Test Variables
A = 1
B = 2
C = 3
S="-hello-"
S *= 3
print(S) 

# OUTPUT: -hello--hello--hello-
```