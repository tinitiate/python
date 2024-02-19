tuple99 = (11, 22, 33, 44, 55, 66)
print('tuple99: ', tuple99) #OUTPUT: tuple99: (11, 22, 33, 44, 55, 66)

# SLice from Index 1 to ONE element before Index 3
print(tuple99[1:3]) # OUTPUT: (22, 33)

# Negative numbers in Index counts from reverse (-1 is last element) 
print(tuple99[-1])  # OUTPUT: 66

# Slice [n:] with no upper bound prints from nth index to end of index(last element)
print(tuple99[2:])  # OUTPUT: (33, 44, 55, 66)