"""
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
myList = [1, 2, 3, 4, 5]
for element_index in range(len(myList)): # range(5)
    print(myList[element_index])  # Prints all the elements in new line


myList = [1, 2, 3, 4, 5]
# Loop through a sub set of list of elements
for element in myList[2:4]:
    print(element)  # Prints all the elements in new line
"""

# Nested Loops, loop inside loop
for outer_loop in range(5):
    for inner_loop in range(5):
        print( outer_loop, '-', inner_loop) 

