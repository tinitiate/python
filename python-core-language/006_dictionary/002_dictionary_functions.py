eats = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}
# Print a value of a key 
print(eats['POTATO']) # OUTPUT: ROOT
print(eats)
# Change a Keys value
eats['POTATO'] = 'VEGETABLE'
print(eats['POTATO']) # OUTPUT: VEGETABLE
print(eats)

# remove one element, key-name: POTATO
del eats['POTATO']

# remove all elements
eats.clear()

# delete dictionary
del eats

#print(eats) # This will result in error.

# Recreate eats
eats = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}

# Get all Keys, returns a list
print(eats.keys())
eats.keys

# Read all elements of a dictionary

for key, value in eats.items():
    print(key, value)
# OUTPUT
#    APPLE FRUIT
#    OKRA VEGETABLE
#    POTATO ROOT