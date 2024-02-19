## Python Class Constructor Built-in Function (__init__)
#* A function, that is executed automatically when
#  the object of the class is created
#* Tt is created using the syntax __init__(self, arguments...)
#* The first argument is "self" always
#* Once a constructor is created all the other functions
#  MUST have the first parameter as "self"
#* "self": is a reference to the object instance

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
tObj1 = ManyValues('A','B','C')
tObj2 = ManyValues(1,2,3,4,5)
