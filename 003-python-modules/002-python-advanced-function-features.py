## >> ---
## >> YamlDesc: CONTENT-ARTICLE
## >> Title: python advanced function features
## >> MetaDescription: python advanced function features code, tutorials
## >> MetaKeywords: python advanced function, nested function,function as a parameter, function as output, features code, tutorials
## >> Author: Venkata Bhattaram / tinitiate.com
## >> ContentName: python-advanced-function-features
## >> ---

## >> # Python python-advanced-function-features

## >> ## Simple Function
## >> * This demonstrates a simple function
## >> ```
# A Simple Function
def Add2Nums(Num1,Num2):
    return Num1+Num2;

# Print the variable
print(Add2Nums(1,2))
## >> ```


## >> ## Nested Function
## >> * Demonstration of a function inside a function, or a nested function
## >> ```
# A Nested Function
# Outer Function "add2numsAndFive"
def add2numsAndFive(num1,num2):
    
    # Inner Function or Nested Function "Add5"
    def Add5(num):
        return num+5;

    return Add5(num1+num2)
# Func-END

# Call the Function add2numsAndFive
print(add2numsAndFive(1,2))
## >> ```


## >> ## Passing function as a parameter to another function
## >> * Demonstration of a Passing function as a parameter to another function
## >> * Passing a Function as a Parameter to Another Function
## >> ```
# Function that "add5" adds 5 to input number`
def add5(num1):
   return num1+5

def addSpl(num1, num2):
    return num1+num2

# Function that Accepts another 
# function as an input parameter
# Parameter Name is "func"
def addTwoNums(func):
    num1 = 1
    num2 = 2
    
    # Return the parameter, by passing another parameter "num1"
    if func == 'add5':
        return func(num1)
        
    elif func == 'addSpl':
        return func(num1, num2)

# Calling "addTwoNums" function with "add5" function 
# as input parameter

print(addTwoNums(add5))
print(addTwoNums(addSpl))
## >> ```


## >> ## Function returns another function as output
## >> * Demonstration of a Function returns another function as output
## >> ```
# Function returns another function as output
# -------------------------------------------
def AddNumWith5(Num1):
    
    # Nested Function
    def Add5():
        return Num1+5

    # Return the "Add5" function
    return Add5

# Capture the Returned function into add_5,
# And add_5 is an object not a variable
add_5 = AddNumWith5(5)

# Printing add_5() is printing as a function
print(add_5())  # OUTPUT: 10

# Printing add_5 is printing as a variable
print(add_5)    # OUTPUT: Some Object Address
## >> ```


## >> ## Function Wrappers
## >> * A Functions "Functionality" can be enhanced without changing the function
## >> * The easy option to enhance a function,
## >>   * Change the Function
## >>   * Call the Function as an Inner Funciton in another function called 
## >>     the wrapper or outer function.
## >> ```
# Parent Function
# This is the function whose function should be enhanced
# ------------------------------------------------------
def AddTWONums(Num1,Num2):
    return Num1+Num2;

# Enhance Functionality by a wrapper function
# Change the parent functions functionality
# Call the funciton "AddTWONums" inside the wrapper
# --------------------------------------------------
def add3Nums_1(Num1,Num2,Num3):

    # Call the parent function inside the add3Nums_1
    return AddTWONums( AddTWONums(Num1,Num2) ,
                       Num3)

# Called the add3Nums_1 function
print(add3Nums_1(1,2,3))
## >> ```
