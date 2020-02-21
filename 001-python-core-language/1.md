---
YamlDesc: CONTENT-ARTICLE
Title: python print statement
MetaDescription: python print statement, c style print, string.format, Print UNICODE, ASCII raw tutorials example code, tutorials
MetaKeywords: python print statement, c style print, string.format, Print UNICODE, ASCII raw tutorials example code, tutorials
Author: Venkata Bhattaram / tinitiate.com
ContentName: print-statement
---

# Print Statement and Comments in Python
* Comments are free text, Any text that is ignored by the compiler,
* Comments are useful to document code and add notes.
* Python supports **SINGLE LINE COMMENTS** and **MULTILINE COMMENTS**
```
# This is a single line comment, Any text followed by a pound or hash symbol "#"
"""
This
is a multiline 
comment
"""
# Any text between TWO LINEs of THREE DOUBLE QUOTES is a multiline comment
```


### Print Statement variations
```
# Simple print statement
print('Welcome to tinitiate.com python turorials');
#OUTPUT: Welcome to tinitiate.com python turorials

# Print statement with append using the "," This appends a SPACE
print('Welcome to tinitiate.com ' , 'python turorials "Appended"');
#OUTPUT: Welcome to tinitiate.com python turorials "Appended"

# Print statement with append using the "+" This Does Not append SPACE
print('Welcome to tinitiate.com' + 'python turorials "Appended"');
#OUTPUT: Welcome to tinitiate.com python turorials "Appended"

# print a single quote, usin esacpe character "\" [backslash]
print('Printing a single quote \'');
#OUTPUT: Printing a single quote '
```


### Print "C language" style
```
# Printing using "C language" style
print('print a double %5.3f' % (1000.23232))
#OUTPUT: print a double 1000.232

# Create variables
strVal = 'tinitiate.com'
intval = 100
print("String= %s Integer= %i" % (strVal, intval))
#OUTPUT String= tinitiate.com Integer= 100
```


### Print statement Using the string.format
* The {} brackets and data enclosed within them are called format fields
* The data is replaced with the objects passed in the str.format() method
* The order by default is left to right as in {} {} and the str.format(Obj1, Obj2)
* The order can be substituted by the numbers {1} {2} for first and second object in
* str.format(Obj1, Obj2)
* The order of the data can also be in the key-values of the
* str.format(key1='value1',key2='value2')
* Sample print {key1} {key2} will be replaced with value1 value2
```
print('Welcome to {} training of {} language'.format('tinitiate.com', 'python'));
#OUTPUT:  Welcome to tinitiate.com training of python language

print('{0} and {1}'.format('tinitiate.com', 'python'))
#OUTPUT:  tinitiate.com and python

print('{1} and {0}'.format('tinitiate.com', 'python'))
#OUTPUT: python and tinitiate.com

print('{siteName} teaches {LanguageName}.'.format(siteName='tinitiate.com', LanguageName='python'))
#OUTPUT: tinitiate.com teaches python.

#Positional and key-value arguments can be arbitrarily combined:
print('The site {0} teaches {LanguageName}'.format('tinitiate.com', LanguageName='Python'))
#OUTPUT: The site tinitiate.com teaches Python
```


### Printing variables
```
#declaring variables for printing
var_integer  = 1                # An integer type variable
var_float    = 10.44            # A float type variable
var_string   = "tinitiate.com"  # A string type variable

print(var_integer, var_float, var_string)
#OUTPUT: 1 10.44 tinitiate.com
```


### Printing a string multiple times, using the "*" operator
```
print ("hello " * 3)
# OUTPUT: hello hello hello 
```


###  printing new line character
```
print("line1" + '\n' + "line2")
# OUTPUT: line1
#         line2  
```


### Print UNICODE and ASCII(raw) strings
```
# Print ASCII using print r<string>
print(r'This is a ASCII string, Has no special characters')

# Print UNICODE using print u<string>
print(u'This is beta (ß), and Has special characters')
```
