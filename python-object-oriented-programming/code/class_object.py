class OOP:

    # Class member = Class Variables or Class Functions

    # Class Variables
    num1 = None
    num2 = None
    num3 = 0

    # Constructor
    def __init__(self,X,Y):
        print(X,Y)
        # Instance variables
        p = X

    # Class Functions
    def add1(self, N1, N2):
        R=N1 + N2
        return R

    def mul1(self, N1, N2):
        return N1 * N2

    def print_class_vars(self):
        print("Class OOPs vars:")
        print("num1",self.num1) # Using/Calling Class variable
        print("num2",self.num2) # Using/Calling Class variable
        print(self.p)           # Using/Calling Instance variable
        # print(self.R)         # CANNOT CALL A FUNCTIONS VAR using "SELF."
        R = self.add1(20,30)


Obj = OOP(11,22)
# WRONG SYNTAX ### Obj.__init__(30,30)
