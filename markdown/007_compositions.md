## YamlDesc: CONTENT-ARTICLE
## Title: python convert dictionary to list, conver dictionary to tuple
## MetaDescription: python read nested list dictionary tuple convert dictionary to list to tuple example code, tutorials
## MetaKeywords: python convert dictionary to list, conver dictionary to tuple example code, tutorials
## Author: Sravya Myla
## ContentName: composition
## ---

# PYTHON Convert Tuple to List to Dictionary

```python
# convert 2 Lists to Dict
# print(dict(zip([x for x in 'abcdefg'], (1,2,3,4,5,6,7,8)))) # tuple
# print(dict(zip([x for x in 'abcdefg'], [1,2,3,4,5,6,7,8])))  # list
# print(dict(zip([x for x in 'abcdefg'],'abcdefg'))) # string

print(dict(zip([x for x in 'abcdefg'], xrange(1, 8))))
```