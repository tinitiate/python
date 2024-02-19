ListOps = [1, 2] 
# Repetition, Printing the List "n" times
print(ListOps*3) # OUTPUT: [1, 2, 1, 2, 1, 2]

# Concatenation, adding another list to the existing list,
# in this case the same list
print(ListOps + ListOps) # OUTPUT: [1, 2, 1, 2]

# Checking if an element is present or not, Using "in" operator
print ('Does element "2" exists in list is ListOps? ', 2 in ListOps) # OUTPUT: True

# Compare lists
list1 = [1, 2]
list2 = [1, 2]
print('The condition list1 == list2 is: ', list1 == list2) # OUTPUT: True 

# Looping and printing over a list
mixedList = [1, 100, 'a', 'ZZ']

# Using for loop to print elements of mixedList 
for element in mixedList:
    print(element)