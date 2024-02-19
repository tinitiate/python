# remove parts of string
# and return the changed string

# strip() Removes the white spaces before and after the string
print (' This is a test  '.strip())
# OUTPUT: This is a test

print ('This is a test'.strip('t')) # removes the last occurrence of 't'
# OUTPUT: This is a tes

print ('This is a test'.strip('T')) # removes the last occurrence of 'T'
# OUTPUT: his is a test

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