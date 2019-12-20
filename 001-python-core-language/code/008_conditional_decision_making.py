## >---
## >YamlDesc: CONTENT-ARTICLE
## >Title: python strings
## >MetaDescription: python conditional statements if else nested if else example code, tutorials
## >MetaKeywords: python, conditional statements, if else, nested if else, example code, tutorials
## >Author: Venkata Bhattaram / tinitiate.com
## >ContentName: conditional-if-else
## >---

## ># PYTHON - CONDITIONAL and DECISION MAKING

## >*  Control flow statements, these are used to execute or not execute 
## >   certain code based on a condition
## >*  if..else
## >*  if<condition1> then..if<condition2> then..
## >   else<default/all other conditions> then..
## >*  nested if..else

## >```
# Simple single IF..ELSE conditional statement syntax
A = 100
B = 100
C = 200

# Check if A = B, and print a message
if A == B:
    print('A and B are same !') # This message will be printed

# Check if B = C, and print a message
if B == C:
    print('B and C are same !') # This will NOT be printed

# Print with ELSE condition
if B == C:
    print('B and C are same !') # This will NOT be printed
else:
    print('B and C are NOT same !') # This will be printed
## >```


## >## Multiple conditions in the same IF
## >```
A = 100
B = 100
C = 200

if A == B and C > A: 
    print('A and B are same and C is greater than A!') # This will NOT be printed
else:
    print('CONDITION DOES NOT MATCH!') # This will NOT be printed


# Nested IF..Else, having multiple conditions
if A == 100:
    print('A is 100') # This will be printed
elif A == 200:
    print('A is 200') # This will NOT be printed
elif A == 200:
    print('A is 200') # This will NOT be printed
else:
    print('A value is something else') # This will NOT be printed
## >```
