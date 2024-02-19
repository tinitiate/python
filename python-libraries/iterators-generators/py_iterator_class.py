# Iterator with a CLASS
# #############################################################################
#* The CLASS provides __ITER__() and __NEXT() functions which provides 
#  the iterator and gets the next value of the iterator.
#* Here we demonstrate a Class with __ITER__() and __NEXT() functions
#  where in a MAX is specified to limit the iterations and until the 
#  MAX is reached it will increment numbers and determine 
#  EVEN or ODD starting with "1".

class EvenOddNumbers:
    
    # Class vars
    # a = 1
    # b = 2

    def __init__(self, max):
        # Instance Vars
        self.max = max
        self.number = 0

    # Override the Iterator to return the class instance
    def __iter__(self):
        return self

    # Return the custom __next__ value specified within this function
    def __next__(self):
    
        # Increment the self.number  once everytime the __next__() is called
        self.number += 1   #== self.number = self.number + 1

        # Exit when the iterations reach the MAX defined in the constructor
        if self.number > self.max:
            print("Max Number of Iterations reached: ", self.max)
        else:
            # Check if the CURRENT number is EVEN or ODD and report it
            if self.number%2 != 0:
                print(str(self.number),"is Odd Number")
            else:
                print(str(self.number),"is Even Number")


# Create an object and call the Class with the MAX value, to end the ITERATOR
obj = EvenOddNumbers(5)

# Call the __next__() of the class more than the Max iterations mentioned 5
obj.__next__()
obj.__next__()
obj.__next__()
obj.__next__()
obj.__next__()
obj.__next__()
obj.__next__()
obj.__next__()