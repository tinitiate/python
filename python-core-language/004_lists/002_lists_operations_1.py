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
print(TestList)


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
#             0  1  2  3  4  5

# 1. Print a part of the list, Slicing a list using ":" operator
#    Also note this Ignores the last INDEX.
print(masterList[1:5]) 
# OUTPUT:  Slicing a list using ":" operator  [2, 3, 4, 5]


# 2. Print for a index to end of string
print('Print masterList elements from index 2 (position(3) to end of string ', masterList[2:]);

# [1, 2, 3, 4, 5, 6]
# 3. Update elements in a list for a given range
masterList[1:4] = ['New1', 'New2', 'New3']
print('Updated masterList: ' ,masterList)
