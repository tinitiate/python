var_test_string = "Python is cool"
# Slicing part of the string using [number:]
# prints string from specified index position to end of string
print(var_test_string[6:])
print("Python is cool"[6:])


# prints string from specified index position to end of string
print(var_test_string[-4:])
print(var_test_string[10:14])

# prints a part of the string between the specified index position
print(var_test_string[4:10])


# OUT oF range indexes
# when specifing indexes that dont exist is a string
# single index usage fails
var_my_string  = "four"
# print(var_my_string[5]) # this is raise an error
# Slicing will not raise error, rather will not print anything 
print(var_my_string[5:7]) # Doesnt print anything 



