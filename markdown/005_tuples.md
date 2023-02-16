---
YamlDesc: CONTENT-ARTICLE
Title: python tuples
MetaDescription: python tuples creating tuple, retrive elements, Operators example code, tutorials
MetaKeywords: python tuples creating tuple, retrive elements, Operators example code, tutorials tuple Methods,find,index example code, tutorials
Author: Sravya Myla
ContentName: tuples
---

# PYTHON Tuples
* Tuple is a immutable(Cannot be changed) group of elements.
* New elements CANNOT be added to a Tuple or Existing ELEMENTS CANNOT 
  be changed in a Tuple.
* Tuple declaration is in curly brackets t = ('data') 
* Tuple is a compound and versatile type.
* Tuples can have elements (values) of mixed data types or same data type 
* Tuple index starts from ZERO
* Tuples support conditional and iterative operations 
* Tuples have built-in functions and methods similar to strings
* Tuples can have elements (values) of mixed data types or same data type 
* Tuples index starts from ZERO
* Tuples Lists support conditional and iterative operations for reading
* Tuples have built-in functions and methods similar to strings


## Crearing, Reading and Deleting Tuples
* Tuples are immutable and cannot be changed
* We cannot change individual elements of tuple
* tuple1[0]=99 # This will result in an error as TUPLES are immutable
* we can overwrite a tuple though
```python
# CREATE TUPLE
tuple1 = (1, 2, 3, 4)
tuple2 = ('A', 'b', 1, 2)

# PRINT TUPLE
print(tuple1)
print(tuple2)

# OUTPUT: (1, 2, 3, 4)
('A', 'b', 1, 2)
```
```python
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)

# OUTPUT: (1, 2, 3, 4, 5)
```
```python
# UPDATE TUPLES
# Easier option for updating parts of tuple are creating 
# new tuples with parts of existing ones
# Create a Tuple with elements 2,3,4 from tuple1
tuple1 = (1, 2, 3, 4, 5)
tuple3=tuple1[1:4]
print(tuple3)

# OUTPUT: (2, 3, 4)
```
```python
# DELETING TUPLES 
tuple1 = (1, 2, 3, 4, 5)
tuple3=tuple1[1:4]
del tuple3
print (tuple3)

# OUTPUT: NameError: name 'tuple3' is not defined.
```
```python
# print(tuple3) # This will throw an error, as this TUPLE doesnt exist
# TUPLES OPERATORS 
# creating a new tuple with appending tuples or concatenating tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (2, 4, 7, 8, 5)
tuple33 = tuple1 + tuple2
print('tuple33: ', tuple33) 

#OUTPUT: tuple33:  (1, 2, 3, 4, 5, 2, 4, 7, 8, 5)
```
```python
tuple34 = (1,2,3) + ('a','b','c') 
print('tuple34: ', tuple34) 

#OUTPUT: tuple34:  (1, 2, 3, 'a', 'b', 'c')
```
```python
# Check if element exists
tuple34 = (1,2,3) + ('a','b','c') 
print(1 in tuple34) 

#OUTPUT: True
```
```python
for LOOP_COUNTER in (1, 2, 3): print(LOOP_COUNTER) 
# OUTPUT: 1
2
3
```
### Multiplication of the tuple values, duplication (multiple times)
```python
tuple1 = (1, 2, 3, 4, 5)
print(tuple1*3) 

# OUTPUT: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
```

## Slicing Tuples
```python
tuple99 = (11, 22, 33, 44, 55, 66)
print('tuple99: ', tuple99) 

#OUTPUT: tuple99: (11, 22, 33, 44, 55, 66)
```
```python
# SLice from Index 1 to ONE element before Index 3
tuple99 = (11, 22, 33, 44, 55, 66)
print(tuple99[1:3])

# OUTPUT: (22, 33)
```
```python
# Negative numbers in Index counts from reverse (-1 is last element) 
tuple99 = (11, 22, 33, 44, 55, 66)
print(tuple99[-1])  

# OUTPUT: 66
```
```python
# Slice [n:] with no upper bound prints from nth index to end of index(last element)
tuple99 = (11, 22, 33, 44, 55, 66)
print(tuple99[2:]) 

# OUTPUT: (33, 44, 55, 66)
```


## Tuples Built-in methods 
```python
tuple99 = (11, 22, 33, 44, 55, 66)
# COUNT method counts the occurrences of an element in the tuple
print((1,1,2,3).count(1)) 

# OUTPUT: 2 
```
```python
# MIN and MAX element of the TUPLE
tuple99 = (11, 22, 33, 44, 55, 66)
print(min(tuple99), max(tuple99)) 

# OUTPUT: 11 66
```
```python
# LENGTH of tuple
tuple99 = (11, 22, 33, 44, 55, 66)
print(len(tuple99))

# OUPUT: 6
```
```python
# SUM of all ELEMENTS
tuple99 = (11, 22, 33, 44, 55, 66)
print(sum(tuple99)) 

# OUTPUT: 231
```
