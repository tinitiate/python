
# PYTHON Convert Tuple to List to Dictionary
* Its essential in many cases to convert complex types to simple types,
* This script demonstrates some examples.  
* Convert TUPLE to LIST.
* Convert TUPLE to DICTIONARY.
* Convert LIST to TUPLE.
* Convert LIST to DICTIONARY.
* Convert DICTIONARY to LIST.
* Convert DICTIONARY to TUPLE.
* Reading values of Nested elements, in List of Tuples
* Reading values of Nested elements, in List of Dictionary

# Converting a TUPLE to a LIST
```python
tuple1 = (1, 2, 3, 4, 5)

# Convert Tuple to List, Use list() Function
tup_list  = list(tuple1)
print(tup_list)  # OUTPUT: [1, 2, 3, 4, 5]
```

# Convert TUPLE to a DICTIONARY
```python
# Convert Tuple of tuples to Dict using dict() Function
tuple1 = ((1, 'a'),(2, 'b'))
dict1 = dict( (y, x) for x, y in tuple1 )
print(dict1)
# {'a': 1, 'b': 2}
```

# Converting LIST to TUPLE
```python
list1 = [1,2,3,4]
tup2 = tuple(list1)
print(tup2)
```

# Converting List to Dictionary
```python
import itertools
list1 = [1,11,2,22,3,33]
dict1 = dict(itertools.zip_longest(*[iter(list1)] * 2, fillvalue=""))
print(dict1)
```

# Convert DICTIONARY to LIST
```python
dict1 = {1:'A', 2:'B', 3:'C'}

# This creates a list of TUPLES
dict_list   = list(dict1.items())

print(dict_list)  # OUTPUT: [(1, 'A'), (2, 'B'), (3, 'C')]
```

# Convert DICTIONARY to LIST of elements
```python
list_tup = [(1, 'A'), (2, 'B'), (3, 'C')]
finalDictionaryBigList=[]

# Loop through the dict_list to create individual tuples
for tuples in list_tup: 
    #Capture individual tuples
    IndividualTuple = tuples
    #Convert individual tuples to lists
    IndividualTuplesList = list(IndividualTuple)
    # Append the IndividualTuplesList to a final List
    finalDictionaryBigList = finalDictionaryBigList + IndividualTuplesList

# Print the final flat list from the dictionary
print(finalDictionaryBigList)
```

# Read nested elements from List of Dictionaries
```python
list_dict = [{'EmpID':1, 'EmpName':'Venkat'},
             {'EmpID':2, 'EmpName':'Sujatha'},
             {'EmpID':3, 'EmpName':'Taran'}]


# Print Name of EmpID: 3
# EmpID: 3 is 3rd element, whose index is "2"
print(list_dict[2]['EmpName'])
```

# Read nested elements from List of Tuples
```python
list_tup = [(1,2),(11,22),(111,222)]

# Print the 3rd Tuple in the list
print(list_tup[2])

# Print the 2nd Element in 2nd Element of the nested tuple
print(list_tup[1][1])
```

