""" MARKDOWN
---
Title: python regular expressions multiple patterns
MetaKeywords: python, regular expressions multiple patterns, code, tutorials
Author: Venkata Bhattaram / tinitiate.com
ContentName: python-regular-expressions-multiple
---
MARKDOWN """

""" MARKDOWN
# PYTHON REGULAR EXPRESSIONS MULTIPLE PATTERNS
* Here we demonstrate use cases for multiple pattern matching in words of 
  a given string.
* Matching Word Pattern "Starts with"
* Matching Word Pattern "Ends with"
* Matching Word Pattern "Has pattern inbetween"
* Matching Word with multiple Patterns (Using an Pattern1 OR Pattern2)
MARKDOWN """
# MARKDOWN ```
import re

my_string = 'Hour01 Min22 VOIDDDDD Sec29 BLAH min3erere Hour32 OTHERS Min33'

"""
# ##############################################################################
# Word Pattern Starts with
# From "my_string" find all words starting with "H"
# ##############################################################################
starting_h = re.findall(r'\bH+\w+.\b', my_string)

for word in starting_h:
    print(word)


# ##############################################################################
# Word Pattern Ends with
# From "my_string" find all words ending with "2"
# ##############################################################################
ending_2 = re.findall(r'\b\w+2\b', my_string)

for word in ending_2:
    print(word)

"""
# ##############################################################################
# Word Pattern has pattern
# From "my_string" find all words those have "3" in them
# ##############################################################################
has_3 = re.findall(r'\w*3\w*', my_string)

for c in has_3:
    print(c)


# ##############################################################################
# Word with multiple Patterns (Using an Pattern1 OR Pattern2)
# From "my_string" find all words those have "ou" OR "OI" in them
# ##############################################################################
has_3 = re.findall(r'\w*OI\w*|\w*ur\w*', my_string)


for c in has_3:
    print(c)
    

# MARKDOWN ```
