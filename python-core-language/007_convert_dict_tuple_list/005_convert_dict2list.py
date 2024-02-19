# Convert DICTIONARY to LIST
dict1 = {1:'A', 2:'B', 3:'C'}

# This creates a list of TUPLES
dict_list   = list(dict1.items())
print(dict_list)  # OUTPUT: [(1, 'A'), (2, 'B'), (3, 'C')]

#convert 2 Lists to Dict
print(dict(zip([x for x in 'abcdefg'], range(1, 8))))
