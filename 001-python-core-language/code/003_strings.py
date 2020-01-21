## >---
## >YamlDesc: CONTENT-ARTICLE
## >Title: python strings
## >MetaDescription: python string, Strings as arrays,Slicing Strings,String Methods,find,index example code, tutorials
## >MetaKeywords: python string, Strings as arrays,Slicing Strings,String Methods,find,index example code, tutorials
## >Author: Venkata Bhattaram / tinitiate.com
## >ContentName: strings
## >---

## ># Python String handling 
## >* In python Strings are sequence of characters in single or double quotes 
## >* Multi-line strings are enclosed in Triple quotes """<Multi Line text>""" 
## >  or '''<Multi Line text>'''
## >* Working with String character index(position of a character in a string)
## >* Strings are immutable, meaning they cant be changed once assogned 
## >  * Slicing strings with INDEX
## >  * String built-in methods
## >  * String text Case conversion
## >  * String Checking methods
## >  * String Manipulation

## >### Strings Basics
## >```
# sample string using DOUBLE QUOTES
var_string_1 = "DOUBLE QUOTES STRING:Welcome to python tutorials by tinitiate.com"

# sample string using SINGLE QUOTES
var_string_2 = 'SINGLE QUOTES STRING: Welcome to python tutorials by tinitiate.com'

# Multi line string using THREE DOUBLE QUOTES
var_string_3 = """THREE DOUBLE QUOTES MULTI LINE STRING: Welcome to python 
tutorials by tinitiate.com,This is a multi line string
as you can see"""

# print the sthe above strings
print(var_string_1)
print(var_string_2)
print(var_string_3)
## >```


## >### Strings as arrays [Using strings as arrays in other languages]
## >```
# Using python strings as STRING ARRAYs
var_test_string = "Python is cool"

# Index starts from 0, 
# This prints the first character of the string 
print('First character of variable var_test_string: ', var_test_string[0]);

# Index of the last character is -1
print('Last character of variable var_test_string: ',var_test_string[-1]);

# Print forth character from the end
print('Fourth character from the end of variable var_test_string: '
       ,var_test_string[-4]); 
## >```


## >### Slicing Strings[ working with string indexes(character positions in the string)]
## >```
var_test_string = "Python is cool"
# Slicing part of the string using [number:]
# prints string from specified index position to end of string
print(var_test_string[6:])

# prints string from specified index position to end of string
print(var_test_string[-4:])

# prints a part of the string between the specified index position
print(var_test_string[4:10])

# OUT oF range indexes
# when specifing indexes that dont exist is a string
# single index usage fails
var_my_string  = "four"
# print(var_my_string[5]) # this is raise an error
# Slicing will not raise error, rather will not print anything 
print(var_my_string[5:7]) # Doesnt print anything 
## >```


## >### String Methods - Text Case conversion
## >```
# Testing String
var_string_case_test = "learn PYTHON"

# upper case conversion
print(var_string_case_test.upper()) # OUTPUT:  LEARN PYTHON

# lower case conversion
print(var_string_case_test.lower()) # OUTPUT:  learn python

# title case conversion
print(var_string_case_test.title()) # OUTPUT:  Learn Python

# swap case conversion, swaps upper to lower and vice versa
print(var_string_case_test.swapcase())  # OUTPUT:  LEARN python

# capitalize case conversion, UPPERs the first letter of the string
print(var_string_case_test.capitalize())  # OUTPUT:  Learn python
## >```


## >### String Methods - Checking methods
## >```
# The Checking methods print true or false (Boolean)
# Checking if the string is UpperCase
print ('PYTHON'.isupper())   # prints true

# Checking if the string is lowerCase
print ('PYTHON'.islower())   # prints false

# Checking if the string is alphabets only
print ('PYTHON01'.islower()) # prints false

# Checking if the string is alphnumeric (alphabets/digits)
print ('PYTHON01'.isalnum()) # prints true

# Checking if the string is alphnumeric (alphabets/digits/special characters)
print ('1000'.isnumeric()) # prints true

# Checking if the string is white space (space/tab)
print ('  '.isspace()) # prints true
## >```


## >### String Methods - String Manipulation
## >```
# remove parts of string
# and return the changed string

# strip() Removes the white spaces before and after the string
print (' This is a test  '.strip())
# OUTPUT: This is a test

print ('This is a test'.strip('t')) # removes the last occurrence of 't'
# OUTPUT: This is a tes

print ('This is a test'.strip('T')) # removes the last occurrence of 'T'
# OUTPUT: his is a tes

print ('This is a test'.lstrip('This')) # removes the last occurrence of 'This'
# OUTPUT:  is a test

# lstrip() Removes the leading characters or white spaces by default 
# white spaces, of a string
# Removes the white spaces before and after the string
print (' This is a test  '.lstrip())
# OUTPUT: This is a test
print ('This is a test  '.lstrip('This'))
# OUTPUT: is a test  

# rstrip() Removes the trailing characters or white spaces by default 
# white spaces, of a string
# Removes the white spaces before and after the string
print ('This is a test  '.rstrip(' test'))
# OUTPUT: This is a
## >```


## >### String alignment justify
## >```
# ljust, center, rjust
# justify methods that add white spaces by default to
# align the string, and pad the string to the length mentioned
print ('test'.ljust(10,'+'))
# OUTPUT: test++++++
print ('test'.rjust(10,'+'))
# OUTPUT: ++++++test
print ('test'.center(10,'+'))
# OUTPUT: +++test+++
## >```


## >### Work with portions of string
## >```
# find()/index(): displays the position index of a given substring and 
# its occurrence number
print ('test'.find('t',2)) # print the index of the second occurrence of 't'
# OUTPUT: 3

print ('test'.index('t')) # print the index of the first occurrence of 't'
# OUTPUT: 0

# find() doesnot raise error, it returns -1 when not found
print ('test'.find('z')) # print the index of the second occurrence of 't'
# OUTPUT: -1

# index(), raises an error when not found
# print ('test'.index('z')) # print the index of the second occurrence of 't'
# ERROR: ValueError: substring not found

#rfind(), prints the highest index and -1 when not found
print ('test'.rfind('z')) # OUTPUT: -1
print ('test'.rfind('t')) # OUTPUT: 3

#rindex(), prints the highest index and errors out when not found
print ('test'.rindex('t')) # OUTPUT: 3

#replace(); replace the characters with the specified characters 
print ('test'.replace('t','i')) # OUTPUT: iesi


#split(), This converts a string into a list based on a separator, 
#default is whitespace 
print('This is a test'.split()) # prints a LIST, seperated by a whitespace
print('This|is|a|test'.split('|')) # prints a LIST,  seperated by a pipe |
print('This,is,a,test'.split(',')) # prints a LIST,  seperated by a comma ,

#splitlines(), Converts multi-line strings to a list
# Test varaible with multi-line string
testString = """Line 1
Line 2
Line 3
"""
print(testString.splitlines()) # OUTPUT: ['Line 1', 'Line 2', 'Line 3']
## >```
