""" MARKDOWN
---
Title: python regular expressions multiple patterns
MetaKeywords: python, regular expressions multiple patterns, code, tutorials
Author: Venkata Bhattaram / tinitiate.com
ContentName: python-regular-expressions-multiple
---
MARKDOWN """

""" MARKDOWN
# PYTHON REGULAR EXPRESSIONS MULTIPLE PATTERNS IN WORDS OF STRING
* Here we demonstrate use cases for multiple pattern matching in words of 
  a given string.
* Matching String Pattern "Starts with"
* Matching String Pattern "Ends with"
* Matching String Pattern "Has pattern inbetween"
* Matching String with multiple Patterns (Using an Pattern1 OR Pattern2)
MARKDOWN """
# MARKDOWN ```
import re

my_string = 'Hour01 Min22 VOIDDDDD Sec29 BLAH min3erere Hour32 OTHERS Min33 Hour32'


# ##############################################################################
# String Pattern Match Exact word
# From "my_string" find all words exactly like "Hour32"
# ##############################################################################
Hour32 = re.findall(r'Hour32', my_string)

for word in Hour32:
    print(word)


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
has_ou_OI = re.findall(r'\w*OI\w*|\w*ur\w*', my_string)

for c in has_ou_OI:
    print(c)

# MARKDOWN ```


""" MARKDOWN
# PYTHON REGULAR EXPRESSIONS MULTIPLE PATTERNS IN STRING
* Here we demonstrate use cases for multiple pattern matching in a given string.
* Matching String Pattern "Starts with"
* Matching String Pattern "Ends with"
* Matching String Pattern "Has pattern inbetween"
* Matching String with multiple Patterns (Using an Pattern1 OR Pattern2)
MARKDOWN """
# MARKDOWN ```
import re

# ##############################################################################
# String Pattern Match with Exact word
# Print "my_string" if exact word "Hour32" is found
# ##############################################################################
my_string = 'Hour01 Min22 VOIDDDDD Sec29 BLAH min3erere Hour32 OTHERS Min33 Hour32'

Hour32 = re.findall(r'Hour32', my_string)

for word in Hour32:
    print(word)


import re

# ##############################################################################
# String Pattern Match with Exact word
# Print "my_string" if exact word "Hour32" is found in it
# ##############################################################################
my_string = 'Hour01 Min22 VOIDDDDD Sec29 BLAH min3erere Hour32 OTHERS Min33 Hour32'

Hour32 = re.search('Hour32', my_string)
if Hour32:
    print(my_string)
    
# ##############################################################################
# String Pattern Starts with
# Print "my_string" if its starts with "H"
# ##############################################################################
starting_h = re.search('H*$', my_string)

if starting_h:
    print(my_string)


# ##############################################################################
# String Pattern Ends with
# Print "my_string" if string ends with "2"
# ##############################################################################
ending_2 = re.search('2$', my_string)

if ending_2:
    print(my_string)


# ##############################################################################
# String with multiple Patterns (Using an Pattern1 OR Pattern2)
# Print "my_string" if there are words with "ou" OR "OI" in them
# ##############################################################################
has_OIur = re.search('OI|ur', my_string)

if has_OIur:
    print(my_string)

# MARKDOWN ```
