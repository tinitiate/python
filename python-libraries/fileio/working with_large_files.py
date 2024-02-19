
# ###########################################################
# Process Very Large Files with Python
# Here we demonstrate working with very large files 

import string
import random
from random import choice
import os 

# STEP 1.
# Create a very large file
# path where large file will be created
l_filename = "E:/code/PYTHON_TRAINING/CODING_PythonLabs/code/001-python-core-language/code/large_data.csv"

with open(l_filename, "w") as flh:
    for c in range(55555):
        row = (''.join(random.choice(string.ascii_uppercase) for i in range(100)) + ",")*50
        flh.write(row[:-1] + "\n")
        # print(row[:-1] + "\n")

# Read Very Large Files with Python
# Here we demonstrate reading with very large file, line by line

# Print File Size in MB
size_in_MB = os.stat(l_filename).st_size / (1024 * 1024)
print("File Size is", size_in_MB,"MB")

# Count the number of lines
# ###############################
l_ctr = 0
with open(l_filename) as infile:
    for line in infile:
        l_ctr=+1

print(l_ctr)

# Remove the File
os.remove(l_filename)
