#===================================================================================
# TOPIC: PYTHON - Regular Expressions basics
#===================================================================================
# NOTES: * Regular Expressions are string patterns to search in other strings
#        * PYTHON Regular Expressions, functionality is provided by the "re" MODULE
#        * The "re" Module provides all the functions required to enable PYTHONs 
#		   regular expressions
#        * Regular expressions is all about matching a "pattern" in a "string" 
#        * search() function, returns true or false for the string found / not found
#        * findall() function, returns a TUPLE of all occurrences of the pattern
#        * sub() function, This is used to replace parts of strings, with a pattern
#        * compile() function, 
#
#===================================================================================
#
# FILE-NAME       : 026_regular_expressions_basics.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Python Regular Expressions
#
#===================================================================================

# First STEP to use Regular Expressions in python import the "re" module
import re

# Create a test string with repeating letters words
test_string = "The Test string 123 121212 tinitiate TINITIATE a1b2c3"


#######################
# 1) search Function
#######################

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

# Prints all the WORDS with a SMALL "t" in the test-string
# The options are:
# word with a "t" in between \w+t\w+,
# OR indicated by the PIPE symbol |
# word with a "t" as the last character \w+t,
# OR indicated by the PIPE symbol |
# word with a "t" as the first character t\w+,
all_t = re.findall(r'\w+t\w+|\w+t|t\w+',test_string)

# The re.findall returns a TUPLE and we print all the elements looping 
# through the tuple
for lpr in all_t:
    print(lpr)


##########################################
# 3) group and groups Function with match
##########################################

# group(), returns the entire matched part of the string
# or the subgroup occurring at the position specified      

t_string = "java python c++ ruby"

# Print all the words having the letter "p" using group

# The match function attempts to match a pattern with the given string
# There are TWO groups in the pattern in curved brackets
SearchObj = re.search(r'([p])(p*\w+)',t_string)

# Prints all the groups of the searchobject 
print("SearchObj.group() : ", SearchObj.group())

# Prints the first group: ([p]) of the searchobject
print("SearchObj.group(1) : ", SearchObj.group(1))

# Prints the second group: (p*\w+) of the searchobject
print("SearchObj.group(2) : ", SearchObj.group(2))


########################
# 4) sub Function
########################

# This is used to replace parts of strings, with a pattern
string = "Tinitiate good python examples"

# Replace "good" with "great"
new_string = re.sub("good", "great", string)
print(string)
print(new_string) 



#===================================================================================
# END OF CODE
#===================================================================================
#TAGS: Python Regular Expressions, build in functions re module
# re.sub re.findall re.search re.group re.groups re.compile
#===================================================================================
