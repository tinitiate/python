## >> ---
## >> YamlDesc: CONTENT-ARTICLE
## >> Title: Python Modules
## >> MetaDescription: Python Modules,Python Modules, __init__.py, __main__.py, __all__, __main__
## >> MetaKeywords: Python Modules,Python Modules, __init__.py, __main__.py, __all__, __main__
## >> Author: Venkata Bhattaram / tinitiate.com
## >> ContentName: python-modules
## >> ---

## >> # Python Modules
## >> * Python Modules are collection of python files placed in one DIRECTORY 
## >>   (With No Spaces), This DIRECTORY name becomes the modules name.
## >> * To use a module, it must be "imported" using the "import" clause, in a 
## >>   python file.
## >> >
## >> * STEPS for Creating a Custom Module
## >> * STEP 1. Create Python Files with Functions and Variables
## >> * STEP 2. Create an empty `__init__.py` file, This indicates that this 
## >>           folder is a module.
## >> * Now this FolderName becomes the "Module Name" and the files in the 
## >> * folder or Module become "importable" in other files. 
## >> * 
## >> * __all__ This is a special "directive"(a string "__all__") that is
## >>   placed in  the __init__.py file, If this is done then when we import 
## >>   the module, Python loads all the modules to the memory.
## >> * __main__.py
## >> * __main__ 


## >> ## Demonstration of Creating a Python Module
## >> * Steps to create a Module
## >> * 1. Create a folder with your module name, say "MathCalc" 
## >> *    [Dont use spaces or spl characters in the folder name]
## >> * 2. Add your python files, say add2nums.py, mul2nums.py, sub2nums.py
## >> * 3. Create an empty file with name __init__.py
## >> *    This makes the folder a module.
## >> * ref. the folder Structure below
## >> ```
#  |-- MathCalc [Folder Name or Module Name]
#  |
#  |---- __init__.py
#  |---- add2nums.py
#  |---- mul2nums.py
#  |---- sub2nums.py
## >> ```

## >> * Create a Folder in say `F:\code\tinitiate\MathCalc`
## >> ```
# mkdir F:\code\tinitiate\MathCalc
## >> ```
## >> >
## >> * Create an **EMPTY** `__init__.py` file in the `MathCalc` folder
## >> >
## >> * Create Three Python Code Files in the `MathCalc` folder, At the command 
## >>   prompt run the following command.
## >> * Create File:  add2nums.py
## >> ```
def add2nums(num1, num2):
    print(num1+num2)
## >> ```
## >> * Create File:  `mul2nums.py`
## >> ```
def mul2nums(num1, num2):
    print(num1*num2)
## >> ```
## >> * Create File:  `sub2nums.py`
## >> ```
def sub2nums(num1, num2):
    print(num1-num2)
## >> ```

## >> ## Test the Module MathCalc
## >> * Create a `ModuleTester.py` to test the module
## >> * The `ModuleTester.py` must be in the same folder as Module Folder
## >> * `F:\code\tinitiate\MathCalc`
## >> * `F:\code\tinitiate\ModuleTester.py`
## >> *
## >> ```
from MathCalc import add2nums, mul2nums, sub2nums

add2nums.add2nums(10,20)
mul2nums.mul2nums(20,30)
sub2nums.sub2nums(40,10)
## >>```

## >> ## Module Python Using __all__ in __init__.py file
## >> * The `__all__` is a list that is placed in the `__init__.py` file, thats 
## >>   part of the Module Folder.
## >> * This List has the member files in the module that need to be made public 
## >>   , This means whe the <module> is imported i.e. when an 
## >>   `from MyModule import *` is called only the files mentioned in the 
## >>   `__all__` list will be accessible from outside the module.
## >> * The below code when added to the `__all__` list in `__init__.py` file, 
## >>   will make the `sub2nums` not accessable in the `ModuleTester.py` file
## >> * Add the following code to the `__init__.py` file to make ONLY 
## >>   `add2nums, mul2nums` public
## >> * Add the following to the __init__.py file
## >> ```
__all__ = [add2nums, mul2nums]
## >> ```

## >> ## Python Module as executable with __main__.py
## >> * Adding a `__main__.py` file in the module folder will make it executable
## >> * A Python program is run by the command line
## >> * Using the module as an executable with `python MathCalc.py`
## >> ```
#  |-- MathCalc [Module Folder Name]
#  |
#  |---- __init__.py [This indicates the folder is a module]
#  |---- __main__.py [Executes when "python website.py" is called at command line]
#  |---- add2nums.py
#  |---- mul2nums.py
#  |---- sub2nums.py
## >> ```
## >> * Add the following to the `__init__.py` file
## >> ```
def main():
    print('main executed')
## >> ```

## >> * Add the following to the `__main__.py` file
## >> ```
if __name__ == '__main__':
    import sys
    import add2nums as a2
    import mul2nums as m2

    if len(sys.argv) != 4:
        print("Enter the Operation Name and values")
        print("add2nums Num1 Num2")
        print("-- OR --")
        print("mul2nums Num1 Num2")
    else:    
        if sys.argv[1] == "add2nums":
            a2.add2nums(int(sys.argv[2]), int(sys.argv[3]))
        elif sys.argv[1] == "mul2nums":
            m2.mul2nums(int(sys.argv[2]), int(sys.argv[3]))
## >> ```

## >> ## Python the __main__ builtin variable
## >> * The __main__ is a special variable, The interpreter reads this variable
## >>   to determine the following
## >>   * The Program run as Module
## >>   * The Module Imported and run in another program
## >> * __main__ is a built in variable that holds the current executing program.
## >> * __name__ is a built in varaible that holds the current program
## >> * **Demonstration**
## >> * Create TWO files `pgm1.py` and `pgm2.py`, here the `pgm1.py` is called 
## >>   from `pgm2.py` and is called directly and the __main__ enables dual behaviour
## >> * File: `pgm1.py`
## >> ```
var1_pgm1 = "Variable 1 of pgm1"
var2_pgm1 = "Variable 2 of pgm1"

def mainFunc():
    if(__name__ == '__main__'):
        print("This code is run as 'python pgm1.py'")
    else:
        print("This code is run as 'import pgm1'")
## >> ```
## >> * File: `pgm2.py`
## >> ```
import pgm1

print(pgm1.mainFunc)
## >>```

## >> ## Accessing Python Modules from other or custom folder path
## >> * To import the Module from a different folder in Python, other path 
## >>   than the caller program.
## >> * Use the `import sys` and the absolute path 
## >> * `sys.path.insert(0, sys.path.insert(0, r'c:\path\to\module-folder'))`
## >> ```
import sys
sys.path.insert(0, sys.path.insert(0, r'c:\path\to\module-folder'))

from MathCalc import add2nums, mul2nums
## >> ```
