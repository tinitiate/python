#========================================================================================================
# TOPIC: PYTHON - Modules
#========================================================================================================
# NOTES: *  Any Python file is a module.
#        *  Module is a file with Python statements, file extension ".py"
#        *  Modules have classes, functions and variables
#        *  Using the ModuleName.FunctionName is the notation to refer to the
#           module objects (classes, functions and variables)
#        *  Modules can import other modules.
#        *  The keyword "import <module-name>" is used to import a module
#        *  The keyword "from <module-name> import <function1>" enables the developer to import 
#           specific objects of a module. 
#        *  Python comes with a library of standard modules
#
#
#========================================================================================================
#
# FILE-NAME       : 013_module.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   013_module.py and 013_module_usage.py
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Python Modules , used to organize code. 
#
#========================================================================================================

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

#========================================================================================================
# END OF CODE
#========================================================================================================
