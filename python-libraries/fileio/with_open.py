### with open() statement to read from a file ###
with open('E:\\python-master\\media\\003-python-modules\\data.csv', 'r') as f:
    contents = f.read()
    print(contents)
"""
### Append to a file using 'a' mode ###
with open('E:\\python-master\\media\\003-python-modules\\data.txt', 'a') as f:
    f.write('Welcome to Tinitiate.\n')

### with open() statement to write to a file ###
with open('E:\\python-master\\media\\003-python-modules\\data.txt', 'w') as f:
    f.write('Hello, Tinitiate!')

### Create a new file using 'x' mode ###
with open('E:\\python-master\\media\\003-python-modules\\data_new.txt', 'x') as f:
    f.write('Welcome to Tinitiate!\n')

### with open() statement to read from a file using 'r+' mode  ###
with open('file.txt', 'r+') as f:
    # Read the file
    data = f.read()
    
    # Write to the file
    f.write('Hello, World!')
"""