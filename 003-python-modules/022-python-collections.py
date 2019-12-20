""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Collections
MetaDescription: Python Collections Counter, defaultdict, OrderedDict, deque, ChainMap, namedtuple()
MetaKeywords: Python Collections Counter, defaultdict, OrderedDict, deque, ChainMap, namedtuple()
Author: Venkata Bhattaram / tinitiate.com
ContentName: python-collections
---
MARKDOWN """

""" MARKDOWN
# Python Collections
* Python Collections are data structures to store data, Similar to the built-ins
  like list, dict, set, tuple etc. These module based collections provide
  additional features. They are part of the **collections** module.
* Python Collections
  * **Counter**
    * Counter is a dict subclass to count the elements of the dictionary.
  * **defaultdict**
    * DefaultDict sets a default value for a new key, this enables a dictionary
      to have  a key with a default value, in the regular dictionary,
      we cannot create a key without a value.
  * **OrderedDict**
    * OrderedDict preserves key order as they are inserted. A regular dict
      does not preserve the insertion order, This can be demonstrated when
      iterating a dictionary.
  * **deque**
    * Deque is like a List where in data can be added from either side,
      data can be removed from either side and data management need not
      be sequential.
  * **ChainMap**
    * ChainMap is used to encapsulates many dictionaries into one unit.
  * **namedtuple()**
    * This is a Tuple (immutable) Give Names to each index in the tuple and
      values can be assigned to those indexes.
MARKDOWN """

# MARKDOWN ```
################################################################################
# Counter
################################################################################
from collections import Counter

# Count Elements in a String
c = Counter('ABCDABCABA')
print(c)

# Count Words in a Sentence
s = 'Python is cool Java is great SQL is cool and great'
words = s.split()
c = Counter(words)
print(c)

# Count elements in a List
L1 = [1,2,3,4,2,3,4,3,4,4]
c = Counter(L1)
print(c)

# Get Most Common using most_common([n])
# Here we get the Top 2 most common occurances of the List elements
L1 = [1,2,3,4,2,3,4,3,4,4]
c = Counter(L1).most_common(2)
print(c)


# Remove Elements using Subtract
L1 = [1,2,3,4,2,3,4,3,4,4]
c = Counter(L1)
L_Remove = {4:2, 3:1}
c.subtract(L_Remove)
print(c)


#  Elements, Is used to convert a Counter to List
L1 = [1,2,3,4,2,3,4,3,4,4]

# Create Counter
c = Counter(L1)

# Use element to convert counter to List
print(sorted(c.elements()))


################################################################################
#Default Dict
################################################################################
from collections import defaultdict

food = defaultdict(lambda: 'Bread')
food['Breakfast'] = 'cereal'
food['Lunch'] = 'Pizza'
print(food['Breakfast'])
print(food['Lunch'])

# Get Value of Key, that doesnt exist
print(food['Dinner'])


################################################################################
#Ordered Dict
################################################################################
from collections import OrderedDict

print("Regular Dict:")
d1 = {}
d1['a'] = 1
d1['b'] = 2
d1['c'] = 3
d1['d'] = 4
d1['e'] = 5

for key, value in d1.items():
    print(key, value)

print("Ordered Dict:")
od1 = OrderedDict()
od1['a'] = 1
od1['b'] = 2
od1['c'] = 3
od1['d'] = 4
od1['e'] = 5

for key, value in od1.items():
    print(key, value)


################################################################################
#Deque
################################################################################
import collections

# initializing deque
dq = collections.deque([1,2,3])

# Add Element on the Right, using append
dq.append(4)

# Add Element on the left, using appendleft()
dq.appendleft(6)

print (dq)

# Remove Element from Right
dq.pop()

# Remove Element from Left
dq.popleft()

print (dq)


################################################################################
#Chain Map
################################################################################
import collections

# initializing dictionaries
e1 = { 'Emp1' : 1, 'Emp2' : 2 }
e2 = { 'Emp3' : 3, 'Emp4' : 4 }

# initializing ChainMap
chain = collections.ChainMap(e1, e2)

# printing chainMap using maps
print(chain.maps)

# printing keys using keys()
print(list(chain.keys()))

# printing keys using keys()
print(list(chain.values()))

# use new_child() to add new dictionary
e3 = { 'Emp5' : 5, 'Emp6' : 6 }
chain = chain.new_child(e3)


################################################################################
#Named Tuple
################################################################################
from collections import namedtuple

employee = namedtuple('employee', 'name, dept, sal')

e1 = employee('AAA', 'Sales', '1000')
print(e1.name)
print(e1.dept)
print(e1.sal)

# MARKDOWN ```
