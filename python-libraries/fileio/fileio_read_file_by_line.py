### Read File Line By Line Using Method readline()
##################################################################
# Read file line by line
# This is a very common requirement, Check contents of a file line 
#  by line and process the data on that line as needed.

import os

# ReOpen the file
l_file_path =  "D:\\training/PythonFeb2024/data.txt"
input_file1 = open(l_file_path,"r")

# While true enter into an infinite loop (we handle it by a break)
while True:
    curr_line = input_file1.readline() # Read line by line, to variable current line
    if not curr_line:
        break                          # Break if there is no line to read
    print(curr_line)                   # Print the current line

# Close the File stream handler
input_file1.close()