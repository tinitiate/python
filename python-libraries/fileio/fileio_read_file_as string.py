## Read File In Python
#########################################################
# Opening and read file in python
# Create a file handler to open the file in READ mode
# using the OPEN function
# The OPEN function returns a file object
# Pass File-Name and the access_mode (Read/Write/Append ..)
import os

l_file_path = "D:\\training/PythonFeb2024/data.txt"
input_file = open(l_file_path,"r")

# Assign the object "input_file" read function
# To a variable
var_text = input_file.read()

# Print the data in one go
print(var_text)

# Close the File stream handler
input_file.close()
