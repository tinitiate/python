# # Read File Line By Line As List Of Strings
# ##############################################
# * Read file line by line as a list of strings, 
#   suffixed with newline character  "\n"

import os
l_file_path = "D:\\training/PythonFeb2024/data.txt"
readlines_file = open(l_file_path,"r")

# Prints the file contents as a LIST
print(readlines_file.readlines())

readlines_file.close()