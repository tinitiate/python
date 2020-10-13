""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: python class
MetaDescription: python class object oriented programming example code, tutorials
MetaKeywords: python, class, objects, object oriented programming, example code, tutorials
Author: Venkata Bhattaram / tinitiate.com
ContentName: print-class
---
MARKDOWN """

""" MARKDOWN
# Object Oriented Programming Vs Functional Programming
* Here we demonstrate why Object Oriented Programming is more efficient than 
  Functional Programming for a same problem-solution
MARKDOWN """

""" MARKDOWN
## Create a Class
* Here we create a Class to Add and Multiply TWO Numbers
MARKDOWN """

# MARKDOWN ```
class oop_calc:

    n1 = None
    n2 = None
            
    def add1(self):
        return self.n1 + self.n2

    def mul1(self):
        return self.n1 * self.n2


# MARKDOWN ```

""" MARKDOWN
## Create the Class Object
* Here we create the class object and display the size of the object
MARKDOWN """

# MARKDOWN ```
from oop_calc import oop_calc

# session f1
# ##############
f1 = oop_calc()
f1.n1 = 100
f1.n2 = 200
print(f1.add1())
print(f1.mul1())


# session f2
# ##############
f2 = oop_calc()
f2.n1 = 1000
f2.n2 = 2000
print(f2.add1())
print(f2.mul1())

print(f1.__sizeof__() + f2.__sizeof__())

# MARKDOWN ```


""" MARKDOWN
## Create a functional code the same as Class
* Here we create a file with functional code, same as the Test Class to Add 
  and Multiply TWO Numbers.
MARKDOWN """

# MARKDOWN ```
n1 = None
n2 = None
        
def add1():
    return n1 + n2

def mul1():
    return n1 * n2
# MARKDOWN ```


""" MARKDOWN
## Import Functionl Code File
* Here we import the Functionl Code File and assign the same values as in 
  the Object Oriented Programming.
* After assigning the values to the functional code caller, it proves that 
  the functionl code occupies more space, and proves that Object Oriented is 
  space efficient in similar business contexts.
MARKDOWN """

# MARKDOWN ```    
import func_test as f1
import func_test as f2

f1.n1 = 100
f1.n2 = 200

f2.n1 = 1000
f2.n2 = 2000

print(f1.__sizeof__() + f2.__sizeof__())
# MARKDOWN ```
