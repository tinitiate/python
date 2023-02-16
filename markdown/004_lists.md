---
YamlDesc: CONTENT-ARTICLE
Title: python lists
MetaDescription: python lists Adding, modifying and removing elements, Operators example code, tutorials
MetaKeywords: python lists Adding, modifying and removing elements, Operators example code, tutorials
Author: Sravya Myla
ContentName: lists
---
# Python Lists
* List is a compound and versatile type.
* In simple words its a List of values or elements, Each element has a 
  position associated with it, the position is called as **Index**,
  The index starts from 0.
* Lists can have elements (values) of mixed data types or same data type 
* Lists are written as comma separated elements enclosed in square 
  brackets, list = ['data']
* List index starts from ZERO
* Lists support conditional and iterative operations for reading
* Lists have built-in functions and methods similar to strings
* Elements can be added to, modified from the List

## Creating and Viewing Lists
```python
# List example
MyNumbersList = [1, 100, 9, 99]
MyStringList  = ["A", 'b', 'Hello', "This"]
# An Empty list
MyList = []
# Adding elements to an empty list
# APPEND adds a Single Element
MyNumbersList = [1, 100, 9, 99]
MyStringList  = ["A", 'b', 'Hello', "This"]
MyList.append(1)
print(MyList)

# OUTPUT: [1]
```

```python
# EXTEND adds multiple Elements
MyNumbersList = [1, 100, 9, 99]
MyStringList  = ["A", 'b', 'Hello', "This"]
# An Empty list
MyList = []
MyNumbersList = [1, 100, 9, 99]
MyStringList  = ["A", 'b', 'Hello', "This"]
MyList.extend([1,2,3,4])
print(MyList)

# OUTPUT: [1, 2, 3, 4]
```

```python
# A Compound elements based list (compound = elements with various data types, here numbers and string)
CompoundList = [1, 100, 'a', 'ZZ']

# Printing a List
print (CompoundList)

# OUTPUT: [1, 100, 'a', 'ZZ']
```

```python
# Printing List element by index
# Index starts from 0 to .. n
# The following prints the first element of the List
CompoundList = [1, 100, 'a', 'ZZ']
print (CompoundList[0])

# OUTPUT: 1
```


## Adding, modifying and removing elements from List
```python
# An empty list
TestList = []
print('Elements of TestList: ', TestList) 

# OUTPUT: Elements of TestList: []
```

```python
# Add elements to a empty list
TestList = [1, 2, 3, 4]
print('Elements of TestList: ', TestList) 

# OUTPUT: Elements of TestList: [1, 2]
```

```python
# Add element in the start to a list
TestList = [1, 2, 3, 4]
TestList.insert(0,99)
print(TestList)

# OUTPUT: [99, 1, 2, 3, 4]
```

```python
# Add element in the end to a list
TestList = [1, 2, 3, 4]
TestList.append(10)
print(TestList)

# OUTPUT: [1, 2, 3, 4, 10]
```

```python
# Modify elements in a list, using the position index of the element
TestList = [1, 2, 3, 4]
TestList[1] = 100

# This changes the SECOND element [ index(1) ] of the list from 2 to 100
TestList = [1, 2, 3, 4]
print('Elements of TestList: ', TestList) 

# OUTPUT: Elements of TestList:  [1, 100, 3, 4]
```

```python
# Removing elements from a list
TestList = [1, 2, 3, 4]
TestList[1] = 100
del TestList[1] # This removed the SECOND element [ index(1) ] of the list: 100
print('Elements of TestList: ', TestList) 

# OUTPUT: Elements of TestList:  [1, 3, 4]
```

```python
# Slicing a LIST using indexes
# -----------------------------
masterList = [1, 2, 3, 4, 5, 6]
# 1. Print a part of the list, Slicing a list using ":" operator
# Also note this Ignores the last INDEX.
print('Slicing a list using ":" operator ' ,masterList[1:5]) 

# OUTPUT:  Slicing a list using ":" operator  [2, 3, 4, 5]
```

```python
# 2. Print for a index to end of string
masterList = [1, 2, 3, 4, 5, 6]
print('Print masterList elements from index 2 (position(3) to end of string ', masterList[2:]);

# OUTPUT: Print masterList elements from index 2 (position(3) to end of string  [3, 4, 5, 6]
```

```python
# 3. Update elements in a list for a given range
masterList = [1, 2, 3, 4, 5, 6]
masterList [1:4] = ['New1', 'New2', 'New3']
print('Updated masterList: ' ,masterList)

# OUTPUT: Updated masterList:  [1, 'New1', 'New2', 'New3', 5, 6]
```

## List Operators 
```python
ListOps = [1, 2] 
# Repetition, Printing the List "n" times
print(ListOps*3) 

# OUTPUT: [1, 2, 1, 2, 1, 2]
```

```python
# Concatenation, adding another list to the existing list,
# in this case the same list
ListOps = [1, 2]
print(ListOps + ListOps) 

# OUTPUT: [1, 2, 1, 2]
```

```python
# Checking if an element is present or not, Using "in" operator
ListOps = [1, 2]
print ('Does element "2" exists in list is ListOps? ', 2 in ListOps) 

# OUTPUT: True
```

```python
# Compare lists
list1 = [1, 2]
list2 = [1, 2]
print('The condition list1 == list2 is: ', list1 == list2) 

# OUTPUT: True 
```

```python
# Looping and printing over a list
mixedList = [1, 100, 'a', 'ZZ']

# Using for loop to print elements of mixedList 
for element in mixedList:
    print(element)

# OUTPUT: 1
100
a
ZZ
```

## List Built-in functions 
```python
newList = [3, 2, 5, 1, 4, 4]

# Length of the LIST
# ------------------
print(len(newList))   
# OUTPUT: 5
print(len([1, 2, 3])) 
# OUTPUT: 3
```

```python
# get Min and Max element in the list
newList = [3, 2, 5, 1, 4, 4]
print(min(newList))  
# OUTPUT: 1
print(max(newList))  
# OUTPUT: 5
print(sum(newList))  
# OUTPUT: 19
```

```python
# Sort a list
newList = [3, 2, 5, 1, 4, 4]
newList.sort()
print(newList) 

# OUTPUT: [1, 2, 3, 4, 4, 5]
```

```python
# Count the occurrences on the passed element
newList = [3, 2, 5, 1, 4, 4]
print(newList.count(4)) 

# OUTPUT: 2
```

```python
# INSERT element before specified index
# usage list.insert(INDEX-VALUE, newElement)
newList = [3, 2, 5, 1, 4, 4]
newList.insert(1, 'A')
print(newList)

# OUTPUT: [1, 'A', 2, 3, 4, 4, 5]
```

```python
# Removes the first occurrence of the specified element
# Throws error if element not found
newList = [3, 2, 5, 1, 4, 4]
newList.remove(4);
print(newList) 

# OUTPUT: [1, 'A', 2, 3, 4, 5]
```
### Reverses the LIST
```python
newList = [3, 2, 5, 1, 4, 4]
newList.reverse()
print(newList) 

# OUTPUT: [5, 4, 3, 2, 'A', 1]
```
### POP an element out of the list
```python
# removes the first or the last element in the list
newList = [3, 2, 5, 1, 4, 4]
newList.pop()
print(newList) 
# OUTPUT: [5, 4, 3, 2, 'A']
```

```python
newList = [3, 2, 5, 1, 4, 4]
newList.pop(0)
print(newList)
# OUTPUT: [4, 3, 2, 'A']
```
### Clear a list
```python
# 1. This remeoves all the elements of the list
newList = [3, 2, 5, 1, 4, 4]
newList.clear()
print(newList) 
# OUTPUT: []

# Reassigning list to empty list [] will clear the list.
newList = []

# OUTPUT: 
```