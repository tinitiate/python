---
YamlDesc: CONTENT-ARTICLE
Title: Python File IO
MetaDescription: Python File IO, Reading Files, Writing to files, create directory, remove directory example code, tutorials
MetaKeywords: Python File IO, Reading Files, Writing to files, create directory, remove directory example code, tutorials
Author: Sravya Myla
ContentName: file-io
---

# PYTHON FILE IO
* The OS Module of Python handles the **FILE IO (File Input Output)**
* Common Folder operations include, List Directories, Find Current 
  Directory Name, Go to a Specific Directory, Create Directory or 
  Delete Directory.
* Common File Operations Include Open a File to Read or Write, Read a File 
  line by line, check if a file exists, Delete a file, Create an empty file.


## Python FILE IO Directory Operations
* The Example demonstrates the following:
  * Display Current Directory 
  * Change to a specified Directory
  * List all files and directories in given path
  * List all files directories **Recursively** in given path
  * Create, Remove Directory
  * List in Directory

### Get Current Directory with getcwd()
* `getcwd()` Displays the Current Directory
```python
import os
print(os.getcwd())

# OUTPUT: Displays the Current Directory
```
>


### Change To Specified Directory With chdir()
* `chdir()` Changes to specified Directory
```python
import os
my_dir = "/Users/sravyamyla/Downloads/"

# Change Directory to the specified name in my_dir
os.chdir(my_dir)

# Check if Current Directory is the one specified in variable "my_dir"
print(os.getcwd())

# OUTPUT: /Users/sravyamyla/Downloads
```

### Python List All Files and Directories in a Given Path
* Using `os.walk()` we can list all Files and Folders in a given folder path 
```python
import os
my_dir = "/Users"
print(os.listdir(my_dir))

# OUTPUT: ['sravyamyla', '.localized', 'Shared']
```
>


### Python List All Files and Directories Recursively in a Given Path
* Using `os.walk()` we can list all Files and Folders in a given folder path 
```python
from os import walk

mypath = "/Users"
all_files = []
all_folders = []

# Loop through all Files and Folders in a Given Path [mypath variable]
for (dirpath, dirnames, filenames) in walk(mypath):
    
    # Capture all files and store in list all_files
    all_files.extend(filenames)
    
    # Capture all files and store in list all_folders
    all_folders.extend(dirnames)

# Print all files and folders lists
print(all_files)
print(all_folders)

OUTPUT: Displays all files and folders
```

### Create Directory Using Method os.mkdir
* Create Directory with `os.mkdir`
```python
import os
# New Directory Path
new_dir = "f:\\NewDir"
# Create Directory with msdir
os.mkdir(new_dir)
# Check if folder exists
print(os.path.exists(new_dir))

# OUTPUT: True
```

### Remove Directory using method os.rmdir
* Remove Directory with `os.rmdir`
```python
import os

# New Directory Path
new_dir = "f:\\NewDir"
# Create Directory with msdir
os.rmdir(new_dir)
# Check if folder exists
print(os.path.exists(new_dir))

# OUTPUT: False
```


## Python FILE IO File Operations
* The following example demonstrates
* Using the OPEN function we can specify a FILE and the
  FILE-MODE(READ, WRITE, APPEND ..)
* Python Reading and writing to files
* Python Opening files
* Python Reading files line by line
* Python writing to files
* Python writing to files line by line
* Check if File Exists
* Create Empty File


## Read File In Python
* Opening and read file in python
* Create a file handler to open the file in READ mode
* using the OPEN function
* The OPEN function returns a file object
* Pass File-Name and the access_mode (Read/Write/Append ..)
 ```python
import os
input_file = open("/Users/sravyamyla/Downloads/code/Bills_new.json","r")
# Assign the object "input_file" read function
# To a variable
var_text = input_file.read()

# Print the data in one go
print(var_text)

# Close the File stream handler
input_file.close()

# OUTPUT: "{\"BillNumber\": 1245, \"BillTotal\": 3000, \"StoreLocation\": \"New York\", \"BillDetails\": [{\"Quantity\": 10, \"UnitPrice\": 2, \"LineItemPrice\": 20}, {\"Quantity\": 5, \"UnitPrice\": 3, \"LineItemPrice\": 15}, {\"Quantity\": 4, \"UnitPrice\": 5, \"LineItemPrice\": 20}]}"
 ```


### Read File Line By Line Using Method readline()
* Read file line by line
* This is a very common requirement, Check contents of a file line 
  by line and process the data on that line as needed.
 ```python
import os
# ReOpen the file
input_file1 = open("/Users/sravyamyla/Downloads/code/Bills_new.json","r")

# While true enter into an infinite loop (we handle it by a break)
while True:
    curr_line = input_file1.readline() # Read line by line, to variable current line
    if not curr_line:
        break                          # Break if there is no line to read
    print(curr_line)                   # Print the current line

# Close the File stream handler
input_file1.close()

# OUTPUT: "{\"BillNumber\": 1245, \"BillTotal\": 3000, \"StoreLocation\": \"New York\", \"BillDetails\": [{\"Quantity\": 10, \"UnitPrice\": 2, \"LineItemPrice\": 20}, {\"Quantity\": 5, \"UnitPrice\": 3, \"LineItemPrice\": 15}, {\"Quantity\": 4, \"UnitPrice\": 5, \"LineItemPrice\": 20}]}"
 ```


### Read File Line By Line As List Of Strings
* Read file line by line as a list of strings, 
  suffixed with newline character  "\n"
 ```python
import os
readlines_file = open("/Users/sravyamyla/Downloads/code/Bills_new.json","r")

# Prints the file contents as a LIST
print(readlines_file.readlines())

readlines_file.close()

# OUTPUT: ['"{\\"BillNumber\\": 1245, \\"BillTotal\\": 3000, \\"StoreLocation\\": \\"New York\\", \\"BillDetails\\": [{\\"Quantity\\": 10, \\"UnitPrice\\": 2, \\"LineItemPrice\\": 20}, {\\"Quantity\\": 5, \\"UnitPrice\\": 3, \\"LineItemPrice\\": 15}, {\\"Quantity\\": 4, \\"UnitPrice\\": 5, \\"LineItemPrice\\": 20}]}"']
 ```



### Write To File In Python
* OPEN() Function, Reading files using PYTHON, Writing to files using PYTHON
* This is a built-in function used to wor with files
* USAGE: FILE_OBJECT = OPEN ("File_path\File_name",FILE_MODE)
* FILE_MODE:
  * "r" READ Mode
  * "w" WRITE Mode (overwrite the file)
  * "a" APPEND Mode (Appends to a file)
  * "r+" READ and WRITE mode
 ```python
import os

# Create a file handler to create a new file in WRITE mode
# USAGE OF THE DOUBLE \\ is for ESCAPING the single "\"
# STEP 1: Create Folder if doesnt exist and ignore if exists
try:
    os.mkdir("/Users/sravyamyla/Downloads/code")
except:
    pass

# STEP 2: Create a file in Write Mode 
new_file = open("/Users/sravyamyla/Downloads/code/Bills_Updated.json", "w")

# STEP 3: Write to file using write method
new_file.write("Welcome to Tinitiate.COM\n")
new_file.write("Line 2 data\n")
new_file.write("Line 3 data\n")
new_file.close()

# OUTPUT: new filw will be created with lines
Welcome to Tinitiate.COM
Line 2 data
Line 3 data
 ```


### APPEND TO EXISTING FILE
```python
# Writing a LIST to file in PYTHON
append_file = open("/Users/sravyamyla/Downloads/code/random.txt","a")

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

# OUTPUT: a file with text 
aZZAbAPPLEPOTATOOKRA
 ```



### Delete A File In Python
* Use the **remove** method to remove or delete file
 ```python
import os
os.remove("/Users/sravyamyla/Downloads/code/random.txt" )

# OUTPUT: File will be removed
 ```


### Rename a file or folder in PYTHON
* The **rename** method can be used to rename both a folder or a file
```python
import os

### Rename a file or folder in PYTHON
# rename a file in PYTHON
# rename c:\tinitiate\data.txt to c:\tinitiate\info.txt
os.rename("/Users/sravyamyla/Downloads/code/random.txt", "/Users/sravyamyla/Downloads/code/info.txt")

# OUTPUT: random.txt will be renamed as info.txt
 ```

