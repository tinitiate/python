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

"""
#split(), This converts a string into a list based on a separator, 
#default is whitespace 
print('This is a test'.split()) # prints a LIST, seperated by a whitespace
print('This|is|a|test'.split('|')) # prints a LIST,  seperated by a pipe |
print('This,is,a,test'.split(',')) # prints a LIST,  seperated by a comma ,

#splitlines(), Converts multi-line strings to a list
# Test varaible with multi-line string
testString = ""Line 1
Line 2
Line 3
""
print(testString.splitlines()) # OUTPUT: ['Line 1', 'Line 2', 'Line 3']

"""