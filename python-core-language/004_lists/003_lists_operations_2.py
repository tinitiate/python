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

