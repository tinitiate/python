# Nested If Else
A = 100
B = 100
C = 200

if A == B and C > A: 
    print('A and B are same and C is greater than A!') # This will NOT be printed
else:
    print('CONDITION DOES NOT MATCH!') # This will NOT be printed

A = 200

# Nested IF..Else, having multiple conditions
print("Before If Block")
if A == 100:
    print('A is 100') # This will be printed
elif A == 200:
    print('Case 1: A is 200') # This will NOT be printed
elif A == 200:
    print('Case 2: A is 200') # This will NOT be printed
else:
    print('A value is something else') # This will NOT be printed
print("After If Block")    