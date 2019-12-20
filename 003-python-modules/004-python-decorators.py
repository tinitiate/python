""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Decorators
MetaDescription: Python Decorators BuiltIn and Custom Decorators
MetaKeywords: Python Decorators BuiltIn and Custom Decorators, @STATICMETHOD @CLASSMETHOD
Author: (c) Venkata Bhattaram / tinitiate.com
ContentName: python-decorators
---
MARKDOWN """

""" MARKDOWN
# PYTHON DECORATORS
* Decorators are a feature that adds functionality to an existing piece of code.
* They act as a wrapper to an existing function, modifying its behavior.
* Also called as metaprogramming, The wrapping action happens at the compile time.
MARKDOWN """

""" MARKDOWN
## Python Built-in Class Decorators
* Creating Static and class methods
* Python provides a mechanism to call class functions WITHOUT creating a class
  Object, This is done through 2 Decorators @staticmethods and @classmethod
* Any function 'decorated' with @staticmethod is callable without instantiating
  the class. It’s definition is immutable via inheritance.
* @staticmethods, is a class decorator, that enables a class function to be used
  without creating an object, This neither accepts a self (the object instance)
  nor the class is implicitly passed as the first argument. They behave like
  plain functions except that you can call them from an instance or the class.
* @classmethod is a decorator when used provides a function in a class,
  as the class object to work on instead of the class instance.
* Enables to call a classes method with out creating an object with classmethods,
  the class of the object instance is implicitly passed as the first argument
  instead of self.
MARKDOWN """

# MARKDOWN ```
# Create class with TWO methods
class tinitiate:
    "Class to demonstrate @classmethod and @staticmethod Decorations"

    # Decorated Using the "@classmethod"
    @classmethod
    def class_function(cls, x):
        print(cls, x)

    # Decorated Using the "@staticmethod"
    # No need to pass the "self" (the object instance) for static method
    @staticmethod
    def static_function(x):
        print(x)


# Create an object of the class tinitiate
obj = tinitiate()

# Call the "CLASS_FUNCTION" using the object
obj.class_function("Class Object Test")

# Call the "STATIC_FUNCTION" using the object
obj.static_function("Static Object Test")

# Call the "STATIC_FUNCTION" directly without the object
tinitiate.static_function("Static Test")

# Call the "CLASS_FUNCTION" directly without the object
tinitiate.class_function("Class Test")
# MARKDOWN ```



""" MARKDOWN
## Python User defined Decorators
* Demonstration of **Callable Function**, Changes behaviour of an existing Function
* Demonstration of User defined Decorators to Change behaviour of an existing Function
* Demonstration of Multiple Decorators that are chained in Python
MARKDOWN """
# MARKDOWN ```
# ##########################################
# Callable Function 
# Changes behaviour of an existing Function
# ##########################################

def EmployeeDiscount(bill_amount):
   return bill_amount - 15

def StudentDiscount(bill_amount):
   return bill_amount - 10


def ApplyCoupon(bill_amount, func):
    
    final_amount = func(bill_amount)
    print(final_amount)


ApplyCoupon(100, EmployeeDiscount)
ApplyCoupon(100, StudentDiscount)


# ##########################################
# Decorators
# Implementing the same using Decorators 
# ##########################################
def EmpDiscount(func):
   def inner(bill_amount): # inner or use any name
      print("Applying Employee Discount")
      return func(bill_amount - 15)
   return inner

def StuDiscount(func):
   def inner(bill_amount):
      print("Applying Student Discount")
      return func(bill_amount - 10)
   return inner


# ############################################
# Create Functions with Decorators
# Create OneFunction for each of the Decorator
# ############################################
@EmpDiscount   
def CouponApply1(bill_amount):
    print(bill_amount)

@StuDiscount   
def CouponApply2(bill_amount):
    print(bill_amount)

# Test the Decorators
CouponApply1(100)
CouponApply2(100)


# #############################################
# Chaining Decorators
# Multiple decorators can be chained in Python
# #############################################
@EmpDiscount
@StuDiscount
def CouponApply3(bill_amount):
    print(bill_amount)


# Test the Decorators
CouponApply3(100)
# MARKDOWN ```


""" MARKDOWN
## Python Custom Decorators with Parameters or Arguments
* We can pass arguments to a Decorator and also change the data that goes into 
  the base function which uses the decorator.
* Below we demonstrate applying `coupons` using Decorators.
MARKDOWN """
# MARKDOWN ```

# CREATE DECORATOR WITH ARGUMENT
################################
def decorator_coupon(N1):
    def wrap(f):
        def wrapped_f(A):
            return f(A - N1)
        return wrapped_f
    return wrap    


# USE DECORATOR WITH FUNCTION DECLARATION
@decorator_coupon(15)
def GetFinalPrice1(A):
    print(A)

@decorator_coupon(25)
def GetFinalPrice2(A):
    print(A)


# Applying Multiple Decorators on a single function declaration
@decorator_coupon(15)
@decorator_coupon(25)
def MultipleCoupons(A):
    print(A)
    


# CALL THE FUNCTION WITH DECORATOR
GetFinalPrice1(100)
GetFinalPrice2(100)
MultipleCoupons(100)

# MARKDOWN ```
