# Modules in Python
* A module in Python is a file containing Python code that can define functions, classes, and variables.
* Modules are used to organize and break down your code into smaller, reusable components.
* They allow you to encapsulate related functionalities and keep your codebase organized, making it easier to manage and maintain.
*  Modules are **import'ed** to other python files or other python modules.

## Creating a Module
* To create a module, you simply create a Python file with a .py extension.
* For example, you can create a file named **my_module.py**
* Inside this file, you can define functions, classes, and variables just like you would in any other Python script.
*  The keyword "import <module-name>" is used to import a module
*  The keyword "from <module-name> import <function1>" enables the developer to import 
   specific objects of a module. 
*  Python comes with a library of standard modules
* Creating a **module** file **my_module.py**
```python
# Creating a Module
# Declare GLOBAL Variables
# Some variables
country_1 = "USA"
country_2 = "China"
country_3 = "India"

# GLOBAL list
list_world_nations = ["USA", "China", "India"]

# GLOBAL tuple
tuple_world_nations = ("USA", "China", "India")

# GLOBAL dictionary
dictionary_world_nations = {'Country_1':'USA', 'Country_1':'China', 'Country_1':'India'}

# Module Function WITHOUT a return type
def module_function_add(in_number1, in_number2):
    "This function add the two input numbers"
    return in_number1 + in_number2
```

## Using a Module
* To use the functions, classes, and variables defined in a module, you need to import the module into your script or interactive session.

```python
# Use this to import the module named "module"
import module

# Using the module's variables and functions

# print the "MODULE" variables, use"module."  -->DOT
print (module.country_1, module.country_2, module.country_3);

# print the "MODULE" LIST
print (module.list_world_nations);

# print the "MODULE" TUPLE
print (module.tuple_world_nations);

# print the "MODULE" DICTIONARY
print (module.dictionary_world_nations);

# calling the function from the module
print (module.module_function_add(1, 3));

```

## Benefits of Using Modules
* **Code Organization:** Modules help organize your code into logical components, improving readability and maintainability.
* **Code Reusability:** Functions and classes defined in modules can be reused across different parts of your program or even in different projects.
* **Collaboration:** Modules allow multiple developers to work on different parts of a project simultaneously without interfering with each other's code.
* **Encapsulation:** You can encapsulate related code and hide implementation details, exposing only what's necessary to the user.

