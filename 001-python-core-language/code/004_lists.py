## >---
## >YamlDesc: CONTENT-ARTICLE
## >Title: python lists
## >MetaDescription: python lists Adding, modifying and removing elements, Operators example code, tutorials
## >MetaKeywords: python lists Adding, modifying and removing elements, Operators example code, tutorials
## >Author: Venkata Bhattaram / tinitiate.com
## >ContentName: lists
## >---

## ># Python Lists
## >* List is a compound and versatile type.
## >* In simple words its a List of values or elements, Each element has a 
## >  position associated with it, the position is called as **Index**,
## >  The index starts from 0.
## >* Lists can have elements (values) of mixed data types or same data type 
## >* Lists are written as comma separated elements enclosed in square 
## >  brackets, list = ['data']
## >* List index starts from ZERO
## >* Lists support conditional and iterative operations for reading
## >* Lists have built-in functions and methods similar to strings
## >* Elements can be added to, modified from the List


## ># Creating and Viewing Lists
## >```
# List example
MyNumbersList = [1, 100, 9, 99]
MyStringList  = ["A", 'b', 'Hello', "This"]

# An Empty list
MyList = []

# Adding elements to an empty list
# APPEND adds a Single Element
MyList.append(1)
print(MyList)

# EXTEND adds multiple Elements
MyList.extend([1,2,3,4])
print(MyList)

# a Compound elements based list (compound = elements with various data types, here 
# numbers and string)
CompoundList = [1, 100, 'a', 'ZZ']

# Printing a List
print (CompoundList)

# Printing List element by index
# Index starts from 0 to .. n
# The following prints the first element of the List
print (CompoundList[0])
## >```


## >## Adding, modifying and removing elements from List
## >```
# An empty list
TestList = []
print('Elements of TestList: ', TestList) # OUTPUT: Elements of TestList: []


# Add elements to a empty list
#-----------------------------
TestList = [1, 2, 3, 4]
print('Elements of TestList: ', TestList) # OUTPUT: Elements of TestList: [1, 2]


# Add element in the start to a list
# ----------------------------------
TestList.insert(0,99)
print(TestList)


# Add element in the end to a list
# --------------------------------
TestList.append(10)
print(TestList)


# Modify elements in a list, using the position index of the element
# ------------------------------------------------------------------
TestList[1] = 100


# This changes the SECOND element [ index(1) ] of the list from 2 to 100
# -----------------------------------------------------------------------
print('Elements of TestList: ', TestList) 
# OUTPUT: Elements of TestList:  [1, 100, 3, 4]


# Removing elements from a list
# -----------------------------
del TestList[1] # This removed the SECOND element [ index(1) ] of the list: 100
print('Elements of TestList: ', TestList) # OUTPUT: Elements of TestList:  [1, 3, 4]


# Slicing a LIST using indexes
# -----------------------------
masterList = [1, 2, 3, 4, 5, 6]


# 1. Print a part of the list, Slicing a list using ":" operator
#    Also note this Ignores the last INDEX.
print('Slicing a list using ":" operator ' ,masterList[1:5]) 
# OUTPUT:  Slicing a list using ":" operator  [2, 3, 4, 5]


# 2. Print for a index to end of string
print('Print masterList elements from index 2 (position(3) to end of string ', masterList[2:]);


# 3. Update elements in a list for a given range
masterList [1:4] = ['New1', 'New2', 'New3']
print('Updated masterList: ' ,masterList)
## >```



## >## List Operators 
## >```
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
## >```


## >## List Built-in functions 
## >```
newList = [3, 2, 5, 1, 4, 4]

# Length of the LIST
# ------------------
print(len(newList))   # OUTPUT: 5
print(len([1, 2, 3])) # OUTPUT: 3

# get Min and Max element in the list
print(min(newList))  # OUTPUT: 1
print(max(newList))  # OUTPUT: 5
print(sum(newList))  # OUTPUT: 19

# Sort a list
# -----------
newList.sort()
print(newList)  # OUTPUT: [1, 2, 3, 4, 4, 5]


# Count the occurrences on the passed element
# -------------------------------------------
print(newList.count(4)) # OUTPUT: 2


# INSERT element before specified index
# -------------------------------------
# usage list.insert(INDEX-VALUE, newElement)
newList.insert(1, 'A')
print(newList) # OUTPUT: [1, 'A', 2, 3, 4, 4, 5]


# Removes the first occurrence of the specified element
# -----------------------------------------------------
# Throws error if element not found
newList.remove(4);
print(newList) # OUTPUT: [1, 'A', 2, 3, 4, 5]


# Reverses the LIST
# -----------------
newList.reverse()
print(newList) # OUTPUT: [5, 4, 3, 2, 'A', 1]


# POP an element out of the list
# ------------------------------
# removes the first or the last element in the list
newList.pop()
print(newList) # OUTPUT: [5, 4, 3, 2, 'A']

newList.pop(0)
print(newList) # OUTPUT: [4, 3, 2, 'A']


# Clear a list
# -----------
# 1. This remeoves all the elements of the list
newList.clear()
print(newList) # OUTPUT: []

# Reassigning list to empty list [] will clear the list.
newList = []

## >```
