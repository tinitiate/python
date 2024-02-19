# Python Custom Modules as Folder (Multiple Files)
* Python Modules are collection of python files placed in one DIRECTORY 
  (Name with No Spaces), This DIRECTORY name becomes the modules name.
* To use a module, it must be "imported" using the "import" clause, in a 
  python file.
* STEPS for Creating a Custom Module Folder
* STEP 1. Create Python Files with Functions and Variables
* STEP 2. Create an empty `__init__.py` file, This indicates that this          folder is a module.
* Now this FolderName becomes the "Module Name" and the files in the 
* Folder or Module become **importable** in other files. 
* __all__ This is a special "directive"(a string "__all__") that is
  placed in  the __init__.py file, If this is done then when we import 
  the module, Python loads all the modules to the memory.

## Demonstration of Creating a Python Module with multiple files
* Steps to create a Module
    * Create a folder with your module name, say "MathCalc" 
* [Dont use spaces or spl characters in the folder name]
  * Add your python files, say add2nums.py, mul2nums.py, sub2nums.py
  * Create an empty file with name __init__.py
  * This makes the folder a module.
  * ref. the folder Structure below
```
#  |-- MathCalc [Folder Name or Module Name]
#  |
#  |---- __init__.py
#  |---- add2nums.py
#  |---- mul2nums.py
#  |---- sub2nums.py
```

### FOLDER as MODULE
#### Module Code for FOLDER as MODULE
* Create a folder for the module
```bash
mkdir c:\code\MathCalc
```
* Create an **EMPTY** `__init__.py` file in the `MathCalc` folder
* Create Three Python Code Files in the `MathCalc` folder, At the command 
  prompt run the following command.
* Create File:  add2nums.py
```python
def add2nums(num1, num2):
    print(num1+num2)
```
* Create File:  `mul2nums.py`
```python
def mul2nums(num1, num2):
    print(num1*num2)
```
* Create File:  `sub2nums.py`
```python
def sub2nums(num1, num2):
    print(num1-num2)
```

#### Test the Module MathCalc
* Create a `MathCalcCaller.py` to test the module
* The `MathCalcCaller.py` must be in the same folder as Module Folder
* `c:\code\tinitiate\MathCalc`
* `c:\code\tinitiate\MathCalcCaller.py`
```python
from MathCalc import add2nums, mul2nums, sub2nums

add2nums.add2nums(10,20)
mul2nums.mul2nums(20,30)
sub2nums.sub2nums(40,10)
```

### FOLDER as MODULE with __all__ in __init__.py file
#### Code for FOLDER as MODULE with __all__ in __init__.py file
* The `__all__` is a list that is placed in the `__init__.py` file, thats 
  part of the Module Folder.
* This List has the member files in the module that need to be made public 
  , This means whe the <module> is imported i.e. when an 
  `from MathCalcInit_all import *` is called only the files mentioned in the 
  `__all__` list will be accessible from outside the module.
* The below code when added to the `__all__` list in `__init__.py` file, 
  will make the `sub2nums` not accessable in the `ModuleTester.py` file
* Add the following code to the `__init__.py` file to make ONLY 
  `add2nums, mul2nums` public
* Create File: **__init__.py**
```
__all__ = [add2nums, mul2nums]
 ```

## Code for Python Module with multiple files Using __all__ in __init__.py file 
* Create folder for the module code
```bash
mkdir c:\code\MathCalcInit_all
```
* Create File:  **__init__.py**
```python
__all__

# * UnComment the below code if you want to allow only
#   FUNCTION: add2nums, mul2nums to be called by other 
#   pyton files
# __all__ = [add2nums, mul2nums]
```
* Create File:  **add2nums.py**
```python
def add2nums(num1, num2):
    print(num1+num2)
```
* Create File:  **mul2nums.py**
```python
def mul2nums(num1, num2):
    print(num1*num2)
```
* Create File:  **sub2nums.py**
```python
def sub2nums(num1, num2):
    print(num1-num2)
```
* Module Caller file:  **MathCalcInit_all_caller.py**
```python
from MathCalcInit import add2nums, mul2nums, sub2nums

add2nums.add2nums(10,20)
mul2nums.mul2nums(20,30)
sub2nums.sub2nums(40,10)
```


## Python Module: called as executable and called as import
* The if __name__ == "__main__": construct in Python allows a script to be both used by other scripts as a module and also run as a standalone script.
* __main__ is a built in variable that holds the current executing program.
* __name__ is a built in varaible that holds the current program
* Let's break down your request step by step:
* Create a custom module named addition_module.py.
* Inside this module, we'll define a function called add_variables() that adds two variables. When this module is imported elsewhere, it should allow the user to pass values to add.
* **Step 1:** Create the custom module - addition_module.py
```python
# addition_module.py
def add_variables(var1=0, var2=0):
    """Add two variables and return the result."""
    return var1 + var2

if __name__ == "__main__":
    # This block of code will only run if this script is executed directly
    # and not when it's imported as a module.
    
    # You can use this block to test the functionality if needed.
    value1 = int(input("Enter the first number: "))
    value2 = int(input("Enter the second number: "))
    
    result = add_variables(value1, value2)
    print(f"The sum is: {result}")
```
* In the above module:
* We define a function add_variables that takes two variables var1 and var2 with default values of 0.
* The if __name__ == "__main__": block is used to execute the code only if the script is run directly, not when it's imported as a module.
* **Step 2:** Use the custom module in another script or Python shell
Now, you can use the addition_module.py as a module in another script or in the Python interactive shell.
* Here's an example:
```python
# main_scaddition_module_callerript.py
import addition_module

# Using the function from the module with default values
result_default = addition_module.add_variables()
print(f"Default sum is: {result_default}")

# Using the function from the module with custom values
value3 = 5
value4 = 3
result_custom = addition_module.add_variables(value3, value4)
print(f"Custom sum is: {result_custom}")
```
* When you run main_script.py, you'll see both the default and custom sums printed.
* In summary, the if __name__ == "__main__": block allows you to include code that gets executed when you run the script directly but not when you import it as a module.
* This is useful for testing or for including some standalone functionality within a module.


## Python Module Multiple Files: called as executable and called as import
### Python Module as executable with __main__.py
* Create a Folder with name : **MathModule**
* This folder name will be the Module Name.
* Adding a `__main__.py` file in the module folder will make it executable
* A Python program is run by the command line
* Using the module as an executable with `python -m MathModule`
```
#  |-- MathModule [Module Folder Name]
#  |
#  |---- __init__.py [This indicates the folder is a module]
#  |---- __main__.py [Executes when "python -m MathModule" is called at command line]
#  |---- add_variables.py
#  |---- multiply_variables.py
```
* **add_variables.py:** This module will contain the function to add two numbers.
```python
# add_variables.py
def add_variables(var1=0, var2=0):
    """Add two variables and return the result."""
    return var1 + var2
```
multiply_variables.py: This module will contain the function to multiply two numbers.
```python
# multiply_variables.py
def multiply_variables(var1=1, var2=1):
    """Multiply two variables and return the result."""
    return var1 * var2
```

__main__.py: This will be the entry point that demonstrates the functionalities of both modules.
```python
# __main__.py
from math_module import add_variables
from multiplication_module import multiply_variables

def main():
    # Using the add_variables function from math_module
    value1 = int(input("Enter the first number for addition: "))
    value2 = int(input("Enter the second number for addition: "))
    result_add = add_variables(value1, value2)
    print(f"The sum is: {result_add}")

    # Using the multiply_variables function from multiplication_module
    value3 = int(input("Enter the first number for multiplication: "))
    value4 = int(input("Enter the second number for multiplication: "))
    result_multiply = multiply_variables(value3, value4)
    print(f"The product is: {result_multiply}")

if __name__ == "__main__":
    # This block will only execute if this script (__main__.py) is run directly.
    main()
```
* **How to Run:**
* To execute the package as a script and see the functionalities, navigate to the directory containing these files and run:
```bash
# Run using python -m ModuleName
python -m MathModule
```


## Accessing Python Modules from other or custom folder path
* To import the Module from a different folder in Python, other path 
  than the caller program.
* Use the `import sys` and the absolute path 
```python
import sys
sys.path.append('/path/to/module-folder')
```
