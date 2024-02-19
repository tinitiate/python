# CREATE TUPLE
tuple1 = (1, 2, 3, 4)
tuple2 = ('A', 'b', 1, 2)

# PRINT TUPLE
print(tuple1)
print(tuple2)

tuple1 = (1, 2, 3, 4, 5)
print(tuple1)

# UPDATE TUPLES
# Easier option for updating parts of tuple are creating 
# new tuples with parts of existing ones
# Create a Tuple with elements 2,3,4 from tuple1
tuple3=tuple1[1:4]
print(tuple3)

# DELETING TUPLES 
del tuple3
# print(tuple3) # This will throw an error, as this TUPLE doesnt exist

# TUPLES OPERATORS 
# creating a new tuple with appending tuples or concatenating tuples
tuple33 = tuple1 + tuple2
print('tuple33: ', tuple33) #OUTPUT: tuple33:  (1, 2, 3, 4, 5, 'A', 'b', 1, 2)

tuple34 = (1,2,3) + ('a','b','c') 
print('tuple34: ', tuple34) #OUTPUT: tuple34:  (1, 2, 3, 'a', 'b', 'c')

# Check if element exists
print(1 in tuple34) #OUTPUT: True

for LOOP_COUNTER in (1, 2, 3): print(LOOP_COUNTER) 
# OUTPUT: 1
#         2
#         3

# Multiplication of the tuple values, duplication (multiple times)
print(tuple1*3) # OUTPUT: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)