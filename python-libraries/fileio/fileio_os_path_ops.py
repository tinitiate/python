## PYTHON FILE IO
## The OS Module of Python handles the **FILE IO (File Input Output)**
## Common Folder operations include, List Directories, Find Current 
## Directory Name, Go to a Specific Directory, Create Directory or 
## Delete Directory.
## Common File Operations Include Open a File to Read or Write, Read a File 
## line by line, check if a file exists, Delete a file, Create an empty file.

## Python FILE IO Directory Operations
## The Example demonstrates the following:
## * Display Current Directory 
## * Change to a specified Directory
## * List all files and directories in given path
## * List all files directories **Recursively** in given path
## * Create, Remove Directory
## * List in Directory


import os

## Get Current Directory with getcwd()
## getcwd() Displays the Current Directory

print(os.getcwd())

## >### Change To Specified Directory With chdir()
## >* `chdir()` Changes to specified Directory

my_dir = "D:\\training/PythonFeb2024/"

# Change Directory to the specified name in my_dir
os.chdir(my_dir)

# Check if Current Directory is the one specified in variable "my_dir"
print(os.getcwd())

## Create Directory Using Method os.mkdir
# 

# New Directory Path
new_dir = "E:\\Training"

# Check if folder exists
print(os.path.exists(new_dir))


# Create Directory with mkdir
# ###########################
try:
    os.mkdir(new_dir)
except Exception as e:
    print(type(e).__name__, e)

# Check if folder exists
print(os.path.exists(new_dir))


# Remove Directory with rmdir
# ###########################
os.rmdir(new_dir)

# Check if folder exists
print(os.path.exists(new_dir))


my_dir = "D:\\training/PythonFeb2024/"
# List Contents in a Dir
# #######################
print(os.listdir(my_dir))


# Rename a file or folder in PYTHON
# ###################################
# The **rename** method can be used to rename both a folder or a file
# rename c:\tinitiate\data.txt to c:\tinitiate\info.txt
# os.rename(my_dir+"\\newdata.txt" , my_dir+"\\olddata.txt" )

# Delete a file
# ######################################
os.remove(my_dir+"\\olddata.txt" )
