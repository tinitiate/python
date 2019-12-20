# Python Core Language Q and A

## What are the tools that help to find bugs or perform static analysis?
* PyChecker is a static analysis tool that detects the bugs in Python source 
  code and warns about the style and complexity of the bug. Pylint is another 
  tool that verifies whether the module meets the coding standard.

## What are Python decorators?
* A Python decorator is a specific change that we make in Python syntax to 
  alter functions easily.

## How are arguments passed by value or by reference?
* Everything in Python is an object and all variables hold references to the 
  objects. The references values are according to the functions; as a result 
  you cannot change the value of the references. However, you can change the 
  objects if it is mutable.

## What is pass in Python?
* Pass means, no-operation Python statement, or in other words it is a place
  holder in compound statement, where there should be a blank left and nothing 
  has to be written there.

## In Python what are iterators?
* In Python, iterators are used to iterate a group of elements, containers like list.
  Use,`iter` function to convert a data structure into an iterator object
  iter([1,2,3,4])

## What are generators in Python?
* The way of implementing iterators are known as generators.
In a Class override builtin  __iter__ and __next__, to generate a iterable generator
```
class EvenOddNumbers:
    def __iter__(self):
    def __next__(self):
```
* Or use the yield() multiple times in a method to generate an generator object.

## What is docstring in Python?
* A Python documentation string is known as docstring, it is a way of 
  documenting Python functions, modules and classes.

## How you can convert a number to a string?
* In order to convert a number into a string, use the inbuilt function str().
* For octal or hexadecimal representation, use oct() or hex().

## What is the difference between Xrange and range?
* xrange is a sequence object that evaluates lazily, in Python 2
  range() does the same in python 3

## What is module and package in Python?
* In Python, module is the way to structure program. Each Python program file 
  is a module, which imports other modules like objects and attributes.
  The folder of Python program is a package of modules. A package can have 
  modules or subfolders.

## Mention what are the rules for local and global variables in Python?
* Local variables: If a variable is assigned a new value anywhere within the 
  function's body, it's assumed to be local.
  Global variables: Those variables that are only referenced inside a 
  function are implicitly global.

## How can you share global variables across modules?
* To share global variables across modules within a single program, create a 
  special module. Import the config module in all modules of your application.
  The module will be available as a global variable across modules.

## Explain how can you make a Python Script executable on Unix?
* To make a Python Script executable on Unix, you need to do two things,
  Script file's mode must be executable and
  the first line must begin with # ( #!/usr/local/bin/python)

## Mention the use of // operator in Python?
* It is a Floor Divisionoperator , which is used for dividing two operands with 
  the result as quotient showing only digits before the decimal point. 
  For instance, 10//5 = 2 and 10.0//5.0 = 2.0.

## Python environment variables PYTHONSTARTUP, PYTHONCASEOK, PYTHONHOME, PYTHONSTARTUP?
* `PYTHONSTARTUP` It contains the path of an initialization file containing 
  Python source code. It is executed every time you start the interpreter.
  It is named as .pythonrc.py in Unix and it contains commands that load 
  utilities or modify PYTHONPATH
* `PYTHONCASEOK` − It is used in Windows to instruct Python to find the first 
  case-insensitive match in an import statement. Set this variable to any value
  to activate it.
* `PYTHONHOME` − It is an alternative module search path. It is usually embedded
  in the PYTHONSTARTUP or PYTHONPATH directories to make switching module 
  libraries easy.

## What are the file processing modes supported by Python?
* read-only, write-only, read-write and append mode 
  Using “r”, “w”, “rw”, “a” respectively.
* Also supported is text file with “rt”, “wt”, “rwt”, and “at”.
* Also supported is binary file with “rb”, “wb”, “rwb”, “ab”.

## Best approach to open large files for IO?
* Using the with keyword, `with open(MY_LARGE_FILE) as fl:`
