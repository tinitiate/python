# with open()

* The `with open()` statement is a Python expression used to work with files.
* It provides a way to ensure that a file is closed when the block inside the `with` statement is exited, regardless of how the block is exited. 

## `with open()` statement to read from a file

*  We open the file named 'data.txt' for reading using `'r'` as the second argument to `open()`. 
* We use the `read()` method to read the contents of the file 

```python
with open('E:\\python-master\\media\\003-python-modules\\data.txt', 'r') as f:
    contents = f.read()
    print(contents)
```

## Append to a file using 'a' mode

* This will open the file 'data.txt' in append mode (`'a'`), which means that any data written to the file will be appended to the end of the file, rather than overwriting its contents.

```python
with open('E:\\python-master\\media\\003-python-modules\\data.txt', 'a') as f:
    f.write('Welcome to Tinitiate.\n')
```

## `with open()` statement to write to a file

* We open the file named 'data.txt' for writing using `'w'` as the second argument to `open()`. 
* We use the `write()` method to write the string `'Hello, world!'` to the file. 
* Note that if the file already exists, it will be truncated (i.e., its contents will be deleted) before writing to it.

```python
with open('E:\\python-master\\media\\003-python-modules\\data.txt', 'w') as f:
    f.write('Hello, Tinitiate!')

```

## Create a new file using 'x' mode

```python
with open('E:\\python-master\\media\\003-python-modules\\data_new.txt', 'x') as f:
    f.write('Welcome to Tinitiate!\n')
```

## `with open()` statement to read from a file using 'r+' mode

* We open the file 'file.txt' in read-write mode (`'r+'`) and read the entire contents of the file.
* We can then write to the file using the `write()` method.
* When we open a file in read-write mode, the file pointer is initially at the beginning of the file, so any write operations will overwrite the existing data. 

```python
with open('file.txt', 'r+') as f:
    # Read the file
    data = f.read()
    
    # Write to the file
    f.write('Hello, World!')

```

