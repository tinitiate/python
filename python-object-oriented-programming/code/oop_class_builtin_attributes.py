## Python Class Built-in Attributes
#* Object Oriented Programming, in PYTHON
#* Classes in PYTHON have a set of built in attributes and functions
#* Class built-in attributes
#* `__doc__`    Prints the CLASS Documentation string
#* `__name__`   prints the CLASS Name
#* `__module__` module name where the class is defined
#* `__bases__`  base class list in case of Inheritance

# 1. Create a CLASS
###################
class Tinitiate:
    'This is a brief note about the class, This is the TINITIATE Class'
    # a class Variable
    ti_var   = 100
    # a class list
    ti_list  = ["a","b","c"]
    # a class tuple
    ti_tuple = ("x","y","z")
    # a class dictionary
    ti_dictionary = {"1":"A", "2":"b", "3":"c"}

    # a class function
    def ti_function(self):
        "This is a class function"
        print("This is a message from the TINITIATE Class ti_function")


# 2. Using the built-in attributes
##################################
# Create an Object of the Class
tiObject = Tinitiate()

# __doc__ : Prints the CLASS Documentation string
print(tiObject.__doc__)

#__name__ : prints the CLASS Name
print(tiObject.__class__)

# __module__ : module name where the class is defined
print(tiObject.__module__)

# __bases__: base class list in case of Inheritance
print(Tinitiate.__bases__)
