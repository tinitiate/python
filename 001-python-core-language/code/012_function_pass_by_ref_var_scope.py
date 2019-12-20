## >---
## >YamlDesc: CONTENT-ARTICLE
## >Title: python functions
## >MetaDescription: python functions, function with parameters, function with return value example code, tutorials
## >MetaKeywords: python functions, function with parameters, function with return value example code, tutorials
## >Author: Venkata Bhattaram / tinitiate.com
## >ContentName: pass-by-reference-value
## >---

## ># PYTHON FUNCTION ARGUMENTS PASS BY REFERENCE and VALUE, VARIABLE SCOPE
## >* Variables defined inside a function have local scope
## >* Variables defined outside a function have global scope.
## >* Global variables can be accessed inside functions as well.
## >* Function arguments in python are passed by reference, any parameter 
## >  value changed inside the function is reflected outside the call too.
## >* The parameter passed in is actually a reference to a variable (but  
## >  the reference is passed by value)
## >* Caution, when changing arguments by reference make sure to copy the 
## >  contents to a local variable in the function, or else the outer variable
## >  might be overwritten !


## >## Python Global and Local Variables
## >* **Global Variable** is accessable from anywhere in the program, Global 
## >  Variables outside the function are accessable inside the function as well.
## >* **Local Variable** are variables inside a function, They are accessable 
## >  from with in a function and not outside the function.
## >```
MyVar = 'This is a Global Value'

def myFunction():

    # Local Variable
    MyVar = 'This is a local variable'
    
    print('Value of MyVar inside function: ', MyVar)
# End of function code:  myFunction

# Make a call to myFunction
myFunction()
print('Value of MyVar outside function: ', MyVar) 
## >```


## >## Pass by Reference
## >* Function arguments in python are passed by reference, any parameter 
## >  value changed inside the function is reflected outside the call too.
## >```
# Create a source list
source_list = ['A', 'B', 'C']

def function_pass_by_reference(in_list):
    print('function_pass_by_reference says Input List: ', in_list)

    # Changing the input by appending a value to in_list
    in_list.append('D')
    print('function_pass_by_reference says changed List: ', in_list)
# End of function code:  function_pass_by_reference


print('Before passing reference to function, source_list: ', source_list)

# Passing the "source_list" and NOT A COPY of the "source_list"
function_pass_by_reference(source_list)
print('After passing reference to function, source_list: ', source_list)

# OUTPUT
#    Before passing to function, source_list:  ['A', 'B', 'C']
#    Input List:  ['A', 'B', 'C']
#    changed List:  ['A', 'B', 'C', 'D']
#    After passing to function, source_list:  ['A', 'B', 'C', 'D']
## >```


## >### Pass by Value
## >* The parameter passed in is actually a reference to a variable (but  
## >  the reference is passed by value)
## >```
# Create a source list
source_list_2 = ['A', 'B', 'C']

def function_pass_by_value(in_list):
    print('function_pass_by_value says Input List: ', in_list)

    # Reassigning a local value, [pass by value example]
    in_list =[1, 2, 3, 4]
    print('function_pass_by_value says changed List: ', in_list)
# End of function code:  function_pass_by_value


print('Before passing by value to function, source_list: ', source_list_2)

# Passing the "source_list" and NOT A COPY of the "source_list"
function_pass_by_value(source_list_2)
print('After passing by value to function, source_list: ', source_list_2)

# OUTPUT
#    Before passing to function, source_list:  ['A', 'B', 'C']
#    Input List:  ['A', 'B', 'C']
#    changed List:  ['A', 'B', 'C', 'D']
#    After passing to function, source_list:  ['A', 'B', 'C', 'D']
## >```
