""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: python builtin class functions
MetaDescription: python object oriented programming class builtin functions __init__, __iter__ example code, tutorials
MetaKeywords: python, object oriented programming, class builtin functions, example code, tutorials
Author: Venkata Bhattaram / tinitiate.com
ContentName: class-builtin-functions
---
MARKDOWN """

""" MARKDOWN
# Python Class Built-In Functions
* Python Class Built-In Functions, Also called as magic methods, They are 
  default methods whose names when used adds special functionality to the class 
* They are always prefixed and suffixed by double underscores __METHOD__()
MARKDOWN """

""" MARKDOWN
## Python Class Constructor Built-in Function (__init__)
* A function, that is executed automatically when
  the object of the class is created
* Tt is created using the syntax __init__(self, arguments...)
* The first argument is "self" always
* Once a constructor is created all the other functions
  MUST have the first parameter as "self"
* "self": is a reference to the object instance
MARKDOWN """

# MARKDOWN ```
class Tinitiate:
    'This is a brief note about the class, This is the TINITIATE Class'

    
    # a class Variable
    ti_var   = 100

    
    def __init__(self, var1, var2):
        # These are Instance variables
        self.var1 = var1
        self.var2 = var2

    # a class function,"self" holds all the attributes and functions of this class
    # so a reference to any class member can be done easily
    # in here instead of passing var1, var2 we just pass
	# self.( its part of the SYNTAX! )
    def print_member_attributes(self):
        "This class function prints the varibles var1 and var2 from the constructor"
        print("Variables from the CONSTRUCTOR var1: ",self.var1 ," var2:",self.var2)

# OBJECT of the CLASS Tinitiate
tiObject = Tinitiate(1,2)

# Call the CLASS's function
tiObject.print_member_attributes()


# Class with constructor with an ARRAY (unspecified number) of parameters
class ManyValues(object):
    def __init__(self, *args):
        self.items = tuple(args)
        print(self.items)

# This will Print the input parameters as there is a print in the constructor
tObj = ManyValues('A','B','C')
# MARKDOWN ```


""" MARKDOWN
## Python Built-in Function __iter__
* __iter__, This returns a "loop of data"
MARKDOWN """
# MARKDOWN ```
# Create a class with the __init__ method
class IterTest():
    def __init__(self, classList):
        self.classList = classList

    def __iter__(self):
        return (i for i in self.classList)

# Create an object of the Class with a input TUPLE
t_Obj = IterTest(('JAVA','C++', 'SCALA'))


# The result is a loop of elements.
# now iterate over the result
for data in t_Obj:
    print(data)
# MARKDOWN ```


""" MARKDOWN
## Python Built-in Function __del__
* Just like a Constructor, all objects that needs to be freed can be placed in 
  the **Destructor**.
* Usually its used to close connections, close file handler and freeing any 
  shared data or resetting data
MARKDOWN """
# MARKDOWN ```
from os import open

class DestructorDemo:

    def __init__(self):
        print('CONSTRUCTOR: Object of Class DestructorDemo Started')

    # This method, can be used to close all the connections or file handles ..    
    def __del__(self):
        print('DESTRUCTOR: Object of Class DestructorDemo Freed')

x = DestructorDemo()

# MARKDOWN ```


""" MARKDOWN
## Python Built-in Functions __sizeof__, __repr__ and __str__
* `__sizeof__` is a built-in method that returns the internal size in bytes 
  for the given object.
* `__str__` and `__repr__` are both methods for getting a string representation of an object.
* `__str__` built-in function that computes the "informal" string 
  representations of an object, is supposed to be shorter and more user-friendly,
* `__repr__` is a built-in function used to compute the "official" string 
  reputation of an object, It usually longer
MARKDOWN """

# MARKDOWN ```
class ReprStrDemo:

    # Constructor
    def __init__(self, num1, num2):
       self.num1 = num1
       self.num2 = num2

    # repr(), Prints object's variables as string
    def __repr__(self):
       return '%s and %s' % (self.num1, self.num2)

    # repr(), Prints object's variables as string, in eloborate form
    def __str__(self):
       return 'Member Data(%s, %s)' % (self.num1, self.num2)
	   
# Create Object and run STR/REPR
x = ReprStrDemo(1,2)

# Print the String Representation of the class member variables
print(x.__str__());
print(x.__repr__());

# Print the size of the object in bytes
print(x.__sizeof__());
# MARKDOWN ```
