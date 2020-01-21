## >---
## >YamlDesc: CONTENT-ARTICLE
## >Title: python comprehension, create dictionary using zip function
## >MetaDescription: python comprehension, create dictionary, using zip function example code, tutorials
## >MetaKeywords: python comprehension, create dictionary, using zip function example code, tutorials
## >Author: Venkata Bhattaram / tinitiate.com
## >ContentName: comprehension
## >---

## ># PYTHON zip function
## >* Converts TWO lists into list of pairs of tuples
## >* Using loop to Convert lists using zip
## >```
keys = [1,2,3,4,5]
values = ['a','b','c','d','e']

# Create List of Tuples with list and zip
L1 = list(zip(keys,values))
print(L1)

# Create Dictionary with dict and zip
D1 = dict(zip(keys,values))
print(D1)

# Dictionary Comprehension using loop and zip
D2 = dict(zip([x for x in 'abcdefg'], range(8)))
print(D2)

# Dictionary Comprehension using loop and zip
D3 = { k:v for(k,v) in zip(keys, values)}
print(D3)
## >```
