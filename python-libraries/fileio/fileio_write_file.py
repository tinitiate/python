# # Write To File In Python
# ###########################################################################
# OPEN() Function, Reading files using PYTHON, Writing to files using PYTHON
# This is a built-in function used to wor with files
# USAGE: FILE_OBJECT = OPEN ("File_path\File_name",FILE_MODE)
# FILE_MODE:
# * "r" READ Mode
# * "w" WRITE Mode (overwrite the file)
# * "a" APPEND Mode (Appends to a file)
# * "r+" READ and WRITE mode

import os

# Create a file handler to create a new file in WRITE mode
# USAGE OF THE DOUBLE \\ is for ESCAPING the single "\"
l_file_path = "D:\\training/PythonFeb2024/output.txt"

# STEP 2: Create a file in Write Mode 
new_file = open(l_file_path, "w")

# STEP 3: Write to file using write method
new_file.write("Welcome to Tinitiate.COM\n")
new_file.write("Line 2 data")
new_file.write("Line 3 data\n")
new_file.close()

# APPEND TO EXISTING FILE
# #########################################
# Writing a LIST to file in PYTHON

l_file_append_path = "D:\\training/PythonFeb2024/output1.txt"
append_file = open(l_file_append_path,"a")

list_1 = ['a', 'ZZ']
append_file.writelines(list_1)

# Writing a TUPLE to file in PYTHON
tuple_1 = ('A', 'b')
append_file.writelines(tuple_1)

# Writing a DICTIONARY to file in PYTHON
dictionary_1 = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}
append_file.writelines(dictionary_1)

# the close() function will close the file handler
# It flushes all unwritten data to the file
append_file.close
