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
print("learn PYTHON".upper())



# The Checking methods print true or false (Boolean)
# Checking if the string is UpperCase
print ('PYTHON'.isupper())   # prints true

v = 'PYTHON'
print (v.isupper())   # prints true

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

a = True
b = "True"