---
YamlDesc: CONTENT-ARTICLE
Title: python iterative or loops
MetaDescription: python iterative or loops for loop, while loop, loop control, break, continue, pass example code, tutorials
MetaKeywords: python iterative or loops for loop, while loop, loop control, break, continue, pass example code, tutorials
Author: Sravya Myla
ContentName: iterative-loops
---

# PYTHON ITERATIVE or LOOPS
* When a piece of code need to be executed repeatedly, 
  LOOP construct is used.
* Python provides `TWO` loops **FOR LOOP** and **WHILE LOOP**
* NESTED FOR LOOP over number of characters in a string

## PYTHON FOR LOOP
* FOR LOOP, Iterate over a SEQUENCE type (Lists, Tuples, Dictionaries) 
  or Range of numbers
* FOR LOOP over a list
* FOR LOOP over a subset of list
* FOR LOOP over a range of numbers
* FOR LOOP over number of characters in a string
```python
# LOOP 5 times
for c in range(5):
    print('Loop Count: ',c) # Index starts from ZERO !

# LOOP Over the number of characters in a sting
for character in 'MyString':
    print(character) # Prints all the characters in new line

# SYNTAX 1: LOOP over elements in a LIST
myList = [1, 2, 3, 4, 5]
for element in myList:
    print(element)  # Prints all the elements in new line

# SYNTAX 2: LOOP over elements in a LIST
for element_index in range(len(myList)):
    print(myList[element_index])  # Prints all the elements in new line

# Loop through a sub set of list of elements
for element in myList[2:4]:
    print(element)  # Prints all the elements in new line

# Nested Loops, loop inside loop
for outer_loop in range(5):
    for inner_loop in range(5):
        print('outer_loop-inner_loop', outer_loop, '-', inner_loop) 
        # Prints all the elements in new line

# OUTPUT: Loop Count:  0
#Loop Count:  1
#Loop Count:  2
#Loop Count:  3
#Loop Count:  4
#M
#y
#S
#t
#r
#i
#n
#g
#1
#2
#3
#4
#5
#1
#2
#3
#4
#5
#3
#4
#outer_loop-inner_loop 0 - 0
#outer_loop-inner_loop 0 - 1
#outer_loop-inner_loop 0 - 2
#outer_loop-inner_loop 0 - 3
#outer_loop-inner_loop 0 - 4
#outer_loop-inner_loop 1 - 0
#outer_loop-inner_loop 1 - 1
#outer_loop-inner_loop 1 - 2
#outer_loop-inner_loop 1 - 3
#outer_loop-inner_loop 1 - 4
#outer_loop-inner_loop 2 - 0
#outer_loop-inner_loop 2 - 1
#outer_loop-inner_loop 2 - 2
#outer_loop-inner_loop 2 - 3
#outer_loop-inner_loop 2 - 4
#outer_loop-inner_loop 3 - 0
#outer_loop-inner_loop 3 - 1
#outer_loop-inner_loop 3 - 2
#outer_loop-inner_loop 3 - 3
#outer_loop-inner_loop 3 - 4
#outer_loop-inner_loop 4 - 0
#outer_loop-inner_loop 4 - 1
#outer_loop-inner_loop 4 - 2
#outer_loop-inner_loop 4 - 3
#outer_loop-inner_loop 4 - 4
```

## PYTHON WHILE LOOP
* WHILE LOOP, Iterate as long as a condition is true and exit when the
  condition is false 
* PYTHON LOOP CONTROL: BREAK Statement
* PYTHON LOOP CONTROL: CONTINUE Statement
* PYTHON LOOP CONTROL: PASS Statement
```python
# The below syntax loops until curr_value reaches 5
# looping 5 times using while loop 
curr_value = 0                  # SETUP a condition criteria
while (curr_value < 5):
    curr_value += 1  # same as curr_value = curr_value + 1
    print('Curr_value: ', curr_value)    

# OUTPUT: Curr_value:  1
#Curr_value:  2
#Curr_value:  3
#Curr_value:  4
#Curr_value:  5
```

```python
# INFINITE LOOP issue
# great care should be taken when writing loops as it could iterate perpetually or
# run in an infinite loop,while some situations require to run forever like services

# CODE
#  while(1==1)
#      print("in infinite loop")
```

## PYTHON LOOP CONTROL BREAK Statement
* Break clause is used to terminate a loop before loop execution is complete
* Break clause is used to exit from a loop before loop execution is complete
```python
# The following loop exits before  5 iterations
for c in range(5):
    if c == 3:
        break
    print(c)

# Using break with while loop
cur_value = 0                  # SETUP a condition criteria
while (cur_value < 5):
    cur_value += 1  # same as curr_value = curr_value + 1
    if cur_value==3:
        break
    print('Cur_value: ', cur_value)

# OUTPUT: 0
#1
#2
#Cur_value:  1
#Cur_value:  2    
```

## PYTHON LOOP CONTROL CONTINUE Statement
* continue clause ignores all the remaining statements 
  in the current loop iteration and takes control 
 back to the first step in a next loop iteration (if any left)
```python
for c in range(3):
    print('Run:', c,'step1')
    if c==1:
        continue 
    print('Run:', c,'step2')
    print('Run:', c,'step3')

# OUTPUT: Run: 0 step1
#Run: 0 step2
#Run: 0 step3
#Run: 1 step1
#Run: 2 step1
#Run: 2 step2
#Run: 2 step3
```

## PYTHON LOOP CONTROL PASS Statement
* When no action is needed use pass, as it does nothing
* This is very useful as a placeholder for future code
```python
for c in range(3):
    if c==1:
        print('Do a very important step')
    elif c==2:
        pass # DO NOTHING
    else:
        print('normal processing')

# OUTPUT: normal processing
#Do a very important step
```
