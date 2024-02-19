
# Print Statement and Comments in Python
* Comments are free text, Any text that is ignored by the compiler,
* Comments are useful to document code and add notes.
* Python supports **SINGLE LINE COMMENTS** and **MULTILINE COMMENTS**
```
 This is a single line comment, Any text followed by a pound or hash symbol "#"
"""
This
is a multiline 
comment
"""
 Any text between TWO LINEs of THREE DOUBLE QUOTES is a multiline comment
```

# Print Statement variations
```python
# Simple print statement
print('Welcome to tinitiate.com python turorials');

# Print statement with append using the "," This appends a SPACE
print('Welcome to tinitiate.com ' , 'python turorials "Appended"')

# Print statement with append using the "+" This Does Not append SPACE
print('Welcome to tinitiate.com' + 'python turorials "Appended"')

# Print a single quote, usin esacpe character "\" [backslash]
print('Printing a single quote \'');

# OUTPUT: Welcome to tinitiate.com python turorials
# OUTPUT: Welcome to tinitiate.com python turorials "Appended"
# OUTPUT: Welcome to tinitiate.com python turorials "Appended"
# OUTPUT: Printing a single quote '
```

# Print "C language" style
```python
#Printing using "C language" style
print('print a double %5.3f' % (1000.23232))

# Create variables
strVal = 'tinitiate.com'
intval = 100
print("String= %s Integer= %i" % (strVal, intval))

# OUTPUT: print a double 1000.232
# OUTPUT String= tinitiate.com Integer= 100
```

# Print statement Using the string.format or F String
* The {} brackets and data enclosed within them are called format fields
* The data is replaced with the objects passed in the str.format() method
* The order by default is left to right as in {} {} and the str.format(Obj1, Obj2)
* The order can be substituted by the numbers {1} {2} for first and second object in
* str.format(Obj1, Obj2)
* The order of the data can also be in the key-values of the
* str.format(key1='value1',key2='value2')
* Sample print {key1} {key2} will be replaced with value1 value2
```python
print('Welcome to {} training of {} language'.format('tinitiate.com', 'python'))

print('{0} and {1}'.format('tinitiate.com', 'python'))

print('{1} and {0}'.format('tinitiate.com', 'python'))

print('{siteName} teaches {LanguageName}.'.format(siteName='tinitiate.com', LanguageName='python'))

#Positional and key-value arguments can be arbitrarily combined:
print('The site {0} teaches {LanguageName}'.format('tinitiate.com', LanguageName='Python'))

# F String similar to ".format"
l_site = 'tinitiate.com'
l_language_name ='Python'
l_str = f"The site {l_site} teaches {LanguageName}"
pring(l_str)

# OUTPUT:  Welcome to tinitiate.com training of python language
# OUTPUT:  tinitiate.com and python
# OUTPUT: python and tinitiate.com
# OUTPUT: tinitiate.com teaches python.
# OUTPUT: The site tinitiate.com teaches Python
# OUTPUT: The site tinitiate.com teaches Python
```

# Printing variables
```python
# Declaring variables for printing
var_integer  = 1                # An integer type variable
var_float    = 10.44            # A float type variable
var_string   = "tinitiate.com"  # A string type variable

print(var_integer, var_float, var_string)
# OUTPUT: 1 10.44 tinitiate.com
```

# Printing a string multiple times, using the "*" operator
```python
print ("hello " * 3)
# OUTPUT: hello hello hello 
```


#  Printing new line character
```python
print("line1" + '\n' + "line2")
# OUTPUT: line1
#         line2  
```


# Print UNICODE and ASCII(raw) strings
```python 
# Print ASCII using print r<string>
print(r'This is a ASCII string, Has no special characters')

# Print UNICODE using print u<string>
print(u'This is beta (ß), and Has special characters')
```