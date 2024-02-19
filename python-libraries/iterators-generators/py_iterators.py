#  PYTHON ITERATORS
# ######################################################################
# * ITERATORS are looping constructs that can be applied to data containers
#   such as; strings, lists, and dictionaries and even a CLASS by creating
#   an class iterator.
# * The biggest advantage of ITERATORS is there is no boundry, 
#   the loop can be closed in any part of the program (or function)  
# * The ITERATION is done using __next__() function being called one for 
#   each iteration, Once the values are exhausted then calling this 
#   function will throw an error.



### Iterator with __next__() function

# Create a List of Data
data_set1 = [1,2,3,4,5]

# Loop or Iterate over this data list using a Loop
# as List is an iterable object
for value1 in data_set1:
    print(value1)

# Loop or Iterate over this data list using an Iterator
# Create an iterator using the iter function
itr = iter(data_set1)

# Call the print to display the next value
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
# print(itr.__next__())

# This gives an error are there are no more elements
#print(itr.__next__())

# the biggest advantage is there is no "end loop", see for loop indentation
# we can add more code inbetween the ".__next__()" providing some flexibility