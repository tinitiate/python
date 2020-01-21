## >---
## >YamlDesc: CONTENT-ARTICLE
## >Title: python dictionary
## >MetaDescription: python dictionary creating dictionary, retrive elements, Operators example code, tutorials
## >MetaKeywords: python dictionary creating dictionary, retrive elements, Operators example code, tutorials dictionary Methods,find,index example code, tutorials
## >Author: Venkata Bhattaram / tinitiate.com
## >ContentName: dictionary
## >---

## ># Python Dictionary
## >* Dictionaries are associative arrays, unordered set of key:value pairs.
## >* Dictionaries declaration is in flower brackets
## >* d = {'Key1' : 'value1', 'Key2' : 'value2'} 
## >* Dictionaries keys can be any immutable type (Strings and Numbers)
## >* Dictionaries support conditional and iterative operations 
## >* Dictionaries have built-in functions and methods similar to strings


## >## Creating and Viewing a DICTIONARY
## >```

# Create empty Dictionary
dict0 = {}
print(dict0)

# dict1, Key and Value are String
dict1 = {'key1':'Value1', 'key2':'Value2', 'key3':'Value3'}
print(dict1) # OUTPUT: {'key1': 'Value1', 'key2': 'Value2', 'key3': 'Value3'}

eats = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}
print(eats) # OUTPUT: {'OKRA': 'VEGITABLE', 'POTATO': 'ROOT', 'APPLE': 'FRUIT'}
## >```


## >## Adding and Modifying elements of a dictionary
## >```

eats = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}

# Print a value of a key 
print(eats['POTATO']) # OUTPUT: ROOT

# Change a Keys value
eats['POTATO'] = 'VEGETABLE'
print(eats['POTATO']) # OUTPUT: VEGETABLE

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
## >```