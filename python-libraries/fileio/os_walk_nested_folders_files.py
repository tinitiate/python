# ############################################################################
# * Python List All Files and Directories Recursively in a Given Path
# * Using `os.walk()` we can list all Files and Folders in a given folder path 
# ############################################################################
from os import walk

mypath = "E:\\Training\\PythonSep2023"
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
