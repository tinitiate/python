#====================================================================================
# TOPIC: PYTHON - Modules Usage
#====================================================================================
#
# FILE-NAME       : 013_module_usage.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   module.py and 013_module_usage.py
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2013
#
# DESC            : Python Modules , used to organize code. 
#
#====================================================================================

# Use this to import the module named "module"
import module

# Using the module's variables and functions

# print the "MODULE" variables, use"module."  -->DOT
print (module.country_1, module.country_2, module.country_3);
# OUTPUT: USA China India

# print the "MODULE" LIST
print (module.list_world_nations);
# OUTPUT: ['USA', 'China', 'India']

# print the "MODULE" TUPLE
print (module.tuple_world_nations);
# OUTPUT:  ('USA', 'China', 'India')

# print the "MODULE" DICTIONARY
print (module.dictionary_world_nations);
# OUTPUT: {'Country_1': 'India'}

# calling the function from the module
print (module.module_function_add(1, 3));
# OUTPUT: 4


#====================================================================================
# END OF CODE
#====================================================================================
