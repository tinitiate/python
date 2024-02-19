# ############################################### ########################
# Single Inheritance demo, with one parent class and one child class
# Create a PARENT class, which will be inherited by a child class
# ############################################### ########################
class ParentClass():
    Parentvar1 = "parentVariable Value"
    def parentFunction(self):
        print("This is a message from ParentClass.parentFunction")

#This is a clhld class that inherits ParentClass,
# SYNTAX is to call the parent class as a parameter to the child class
class ChildClass(ParentClass):
    ChildVar1 = "parentVariable Value"
    def childFunction(self):
        print("This is a message from ChildClass.childFunction")

# Create an object of the Child Class
cObj = ChildClass()

# CALL CHILDCLASS and PARENTCLASS methods from the child object
cObj.childFunction()
cObj.parentFunction()


# ############################################### ########################
# Example with constructors in both ParentClass with constructor
# ############################################### ########################
class ParentClass:
    ParentVar1 = "parentVariable Value"
    
    def __init__(self, parentVar2):
        self.parentVar2 = parentVar2  # Initialize instance variable in the constructor
    
    def parentFunction(self):
        print("This is a message from ParentClass.parentFunction")

# ChildClass inheriting from ParentClass with constructor
class ChildClass(ParentClass):
    ChildVar1 = "childVariable Value"
    
    def __init__(self, parentVar2, childVar2):
        super().__init__(parentVar2)  # Call the constructor of the ParentClass using super()
        self.childVar2 = childVar2  # Initialize instance variable specific to ChildClass
    
    def childFunction(self):
        print("This is a message from ChildClass.childFunction")

# Create an object of the ChildClass with required parameters for the constructors
cObj = ChildClass("ParentVar2 Value", "ChildVar2 Value")

# Accessing instance variables and methods
print(cObj.parentVar2)  # Output: ParentVar2 Value
print(cObj.childVar2)   # Output: ChildVar2 Value

cObj.childFunction()   # Output: This is a message from ChildClass.childFunction
cObj.parentFunction()  # Output: This is a message from ParentClass.parentFunction
