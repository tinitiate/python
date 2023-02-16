---
Title: Python Working With Large Files
MetaKeywords: Python, Large CSV, Large Files
Author: Sravya Myla
ContentName: python-large -files
---

# Process Very Large Files with Python
* Here we demonstrate working with very large files 
```python

# STEP 1.
# Create a very large file
import string
import random
from random import choice
import os 

l_filename = "/Users/sravyamyla/Downloads/code/data.csv"

with open(l_filename, "w") as flh:
    for c in range(55555):
        row = (''.join(random.choice(string.ascii_uppercase) for i in range(100)) + ",")*50
        flh.write(row[:-1] + "\n")
        # print(row[:-1] + "\n")

# Read Very Large Files with Python
* Here we demonstrate reading with very large file, line by line

# Print File Size in MB
size_in_MB = os.stat(l_filename).st_size / (1024 * 1024)
print("File Size is", size_in_MB,"MB")

# Count the number of lines
l_ctr = 0
with open(l_filename) as infile:
    for line in infile:
        l_ctr=+1

print(l_ctr)

# Remove the File
os.remove(l_filename)

# OUTPUT: File Size is 267.55595207214355 MB
#1

```

