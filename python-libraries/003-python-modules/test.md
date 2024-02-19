---
Title: python iterators and generators
MetaDescription: python regular, expressions, code, tutorials
Author: Venkata Bhattaram / tinitiate.com
ContentName: python-regular-expressions
---


# PYTHON REGULAR EXPRESSIONS BASICS
* Regular Expressions are string patterns to search in other strings
* PYTHON Regular Expressions, functionality is provided by the "re" MODULE
* The "re" Module provides all the functions required to enable PYTHONs
  regular expressions
* Regular expressions is all about matching a "pattern" in a "string"
* **search()** function, returns true or false for the string found / not found
* **findall()** function, returns a TUPLE of all occurrences of the pattern
* **sub()** function, This is used to replace parts of strings, with a pattern
* **split()** function, seperates a string by space or any dilimeter.

```python
#######################
# 1) search Function
#######################
import re

# Create a test string with repeating letters words
test_string = "The Test string 123 121212 tinitiate TINITIATE a1b2c3"

#Search for pattern: tinitiate (in SMALL LETTERS)
match = re.search(r'tinitiate',test_string)

if match:
    print("The word 'tinitiate' is found in the string:", "\n", test_string)
else:
    print("The word 'tinitiate' is NOT found in the string:", "\n", test_string)


# Search for more complicated patterns, search for 12*, where *
# is wildcard character, match everything else after the pattern "12"
match = re.search(r'12*',test_string)

if match:
    print("The word '12*' is found in the string:", "\n", test_string)
else:
    print("The word '12*' is NOT found in the string:", "\n", test_string)


########################
# 2) findall Function
########################
import re

# Prints all the WORDS with a SMALL "t" in the test-string
# The options are:
# word with a "t" in between \w+t\w+,
# OR indicated by the PIPE symbol |
# word with a "t" as the last character \w+t,
# OR indicated by the PIPE symbol |
# word with a "t" as the first character t\w+,

# Create a test string with repeating letters words
test_string = "The Test string 123 121212 tinitiate TINITIATE a1b2c3"

all_t = re.findall(r'\w+t\w+|\w+t|t\w+',test_string)

# The re.findall returns a TUPLE and we print all the elements looping
# through the tuple
for lpr in all_t:
    print(lpr)


########################
# 3) sub Function
########################
import re

# This is used to replace parts of strings, with a pattern
string = "Tinitiate good python examples"

# Replace "good" with "great"
new_string = re.sub("good", "great", string)
print(string)
print(new_string)


########################
# 4) split Function
########################
# The split Function splits a string by spaces
import re

words2list = re.split(r's','Tinitiate good python examples')
print(words2list)

# Split a Comma Seperated String

csv2list = re.split(r',','1,AAA,2000')
print(csv2list)

```
