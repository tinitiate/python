
a = 1
b = -2

print("Before Swap")
print(a)
print(b)

# Swap Code
#
"""
# Solution 1
c = a
a = b
b = c
"""
# Solution 2
a = a+b
b = a-b
a = a-b
#
print("After Swap")
print(a)
print(b)

# String Swap
a_str = "AAA"
b_str = "BBB"

####################################################
# SWAP STRING Vars
####################################################

print("Before Swap")
print(a_str)
print(b_str)
# Swap Code
#
a_str = a_str+b_str # AAABBB
b_str = a_str.rstrip(b_str)
a_str = a_str.lstrip(b_str) 
#
print("After Swap")
print(a_str)
print(b_str)
