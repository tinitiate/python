## Python Built-in Functions __sizeof__, __repr__ and __str__
#* `__sizeof__` is a built-in method that returns the internal size in bytes 
#  for the given object.
#* `__str__` and `__repr__` are both methods for getting a string representation of an object.
#* `__str__` built-in function that computes the "informal" string 
#  representations of an object, is supposed to be shorter and more user-friendly,
#* `__repr__` is a built-in function used to compute the "official" string 
#  reputation of an object, It usually longer

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
