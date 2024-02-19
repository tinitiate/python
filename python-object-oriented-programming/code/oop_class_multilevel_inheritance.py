# ##########################################################################
## Multi-Level Inheritance
#* Here we demonstrate Mult-Level Inheritance, Which is The Inheritance is 
#  across multiple classes where in A Child Class Inherits from a 
#  Parent Class,
#  and the Parent Class inherits from a Grand parent Class
# ##########################################################################

# Create one more parent class, to demonstrate multiple parent inheritance
class GrandParent():
    "This is the GrandParent class"
    def GrandParentFunction(self):
        print("This is a message from the GrandParent.GrandParentFunction")

# This inherits the GrandParent class
class Parent(GrandParent):
    "This is the Parent class"
    def ParentFunction(self):
        print("This is a message from the Parent.ParentFunction")

# Class that inherits Parent Class
class Child(Parent):
    "This is the ChildMI, this inherits Parent_1 and Parent_2"
    def ChildFunction(self):
        print("This is a message from the Child.ChildFunction")

# Create ChildMI Object
gcObj = Child()

gcObj.GrandParentFunction()
gcObj.ParentFunction()
gcObj.ChildFunction()


# ##########################################################################
## Multi-Level Inheritance with constuctors
# ##########################################################################
# Parent_1 class with constructor
class Parent_1:
    "This is another parent-level class"
    
    def __init__(self, parent1Var):
        self.parent1Var = parent1Var  # Initialize instance variable in the constructor
    
    def Parent1Function(self):
        print("This is a message from the Parent_1.Parent1Function")

# Parent_2 class with constructor
class Parent_2:
    "This is another parent-level class"
    
    def __init__(self, parent2Var):
        self.parent2Var = parent2Var  # Initialize instance variable in the constructor
    
    def Parent2Function(self):
        print("This is a message from the Parent_2.Parent2Function")

# Class that inherits from Parent_1 and Parent_2
class ChildMI(Parent_1, Parent_2):
    "This is the ChildMI, this inherits Parent_1 and Parent_2"
    
    def __init__(self, parent1Var, parent2Var):
        Parent_1.__init__(self, parent1Var)  # Initialize Parent_1 using its constructor
        Parent_2.__init__(self, parent2Var)  # Initialize Parent_2 using its constructor
    
    def ChildMIFunction(self):
        print("This is a message from the ChildMI.ChildMIFunction")

# Create ChildMI Object with required parameters for the constructors
gcObj = ChildMI("Parent1Var Value", "Parent2Var Value")

# Accessing instance variables and methods
print(gcObj.parent1Var)  # Output: Parent1Var Value
print(gcObj.parent2Var)  # Output: Parent2Var Value

gcObj.Parent1Function()  # Output: This is a message from the Parent_1.Parent1Function
gcObj.Parent2Function()  # Output: This is a message from the Parent_2.Parent2Function
