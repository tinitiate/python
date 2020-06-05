## >---
## >Title: python comprehensions
## >Keywords: python comprehensions, zip function
## >Author: Venkata Bhattaram
## >---

## ># Python Comprehensions 
## >* Python comprehensions, are shourtcut syntactic constructs that are
## >  used with sets, lists and dictionaries
## >* They can be used to create new lists / dicts from existing lists, based on 
## >  some calculations, filters.

## >## Apply calculations on Lists and Dicts
## >* Python comprehensions enable us to perform calculations on Lists and Dicts
## >  to generete new lists and dicts.
## >```
# Generate New Lists / Dicts based on calculations
##################################################

# Generate list with squares 
list_1 = [5, 6, 7]

# list comprehension
squared_list = [c**2 for c in list_1]
print(squared_list)
# output 
# [25, 36, 49]

# Generate new dict by adding 5 to every value of the dict
add5_dict = {c:c+5 for c in list_1}
print(add5_dict)
# output
# {5: 10, 6: 11, 7: 12}
## >```


## >## Apply Filters and Calculations on Lists and Dicts
## >* Python comprehensions enable us to filter elements of list and perform 
## >  calculations on Lists and Dicts, to generete new lists and dicts.
## >```
# Generate New Lists / Dicts based on filters
#############################################

# Generate new list from the current list after adding 5 to the "even" 
# elements of the 
list_2 = [2, 3, 4, 5]

even_add5_list = [c+5 for c in list_2 if c%2 == 0]
print(even_add5_list)
# output
# [7 ,9]

squared_dict = {c:c+5 for c in list_2 if c%2 != 0}
print(squared_dict)
# output
# {11: 121, 3: 9 , 5: 25 , 7: 49}


## >## Parallel Iterators using zip function
## >* Apply Comprehensions on multiple lists
## >* Converts TWO lists into list of pairs of tuples
## >* Using loop to Convert lists using zip
## >```

# Combine multiple Lists to a single list
#########################################
# Combine sum of multiple lists into a single list
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# Parallel Iteration using ZIP function
list_c = [(x + y) for (x,y) in zip(list_a, list_b)]
print(list_c)
# output
# [5, 7, 9]


# Create a Dict
#################
keys = [1,2,3,4,5]
values = ['a','b','c','d','e']

# Create List of Tuples with list and zip
L1 = list(zip(keys,values))
print(L1)

# Create Dictionary with dict and zip
D1 = dict(zip(keys,values))
print(D1)

# Dictionary Comprehension using loop and zip
D2 = dict(zip([x for x in 'abcdefg'], range(8)))
print(D2)

# Dictionary Comprehension using loop and zip
D3 = { k:v for(k,v) in zip(keys, values)}
print(D3)
## >```
