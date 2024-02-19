
a = 10
print(a)

a = "hello"
print(a)


str1 = "abc"
print(str1[1])


# List example
MyNumbersList = [1, 100, 9, 99]
#                0  1    2  3
print(MyNumbersList[3])

MyStringList  = ["A", 'b', 'Hello', "This"]

# An Empty list
MyList = []

# Adding elements to an empty list
# APPEND adds a Single Element
MyList.append(1)
MyList.append(100)
MyList.append(1000)
print(MyList)


# EXTEND adds multiple Elements
MyList.extend([1,2,3,4])
print(MyList)


# a Compound elements based list (compound = elements with various data types, here 
# numbers and string)
CompoundList = [1, 100, 'a', 'ZZ']

# Printing a List
print (CompoundList)

# Printing List element by index = position
# Index starts from 0 to .. n
# The following prints the first element of the List
print (CompoundList[0])
