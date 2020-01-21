## >---
## >YamlDesc: CONTENT-ARTICLE
## >Title: python functions
## >MetaDescription: python functions parameters arguments, Variable Length arguments, function with parameters, function with return value example code, tutorials
## >MetaKeywords: python functions parameters arguments, Variable Length arguments, function with parameters, function with return value example code, tutorials
## >Author: Venkata Bhattaram / tinitiate.com
## >ContentName: function-parameters
## >---


## ># Python Function Parameters or Arguments
## >* Functions in python support various arguments or parameters
## >  types or styles.
## >* Functions with Regular arguments
## >* Functions with Keyword arguments
## >* Functions with Default arguments
## >* Functions with Variable length arguments


## >### Regular arguments 
## >* This is a regular and straight forward implementation of function argument calls
## >* The parameters supplied when calling the function are in the same order
## >  positional of, the what in which the parameters are declared
## >* To use arguments in any order simply use the argument name when 
## >  calling the function
## >* The arguments can be placed out of order, this is because Python interpreter 
## >  reads through the keywords (positional parameters) provided to match
## >  parameter-values
## >```
def function_with_regular_arguments(arg1, arg2):
    print(arg1+arg2)
    return
# End of function code: function_with_regular_arguments

# Calling the function function_with_regular_arguments
function_with_regular_arguments('Pyt','hon')
# OUTPUT: Python

function_with_regular_arguments('hon','pyt')
# OUTPUT: honpyt
# Order if supplying arguments matters in the regular call, since the calls are 
# made by position of the arguments

function_with_regular_arguments(arg2='hon', arg1='pyt')
# OUTPUT: Python
## >```


## >### Default arguments 
## >* Python supports a default value for an argument, which assumes a default value 
## >  (thats part of the function definition), when the value for that argument 
## >  is not provided
## >* The below function has 2 parameters "arg1" and "default_arg2", with a default  
## >  value for "default_arg2" of 100.
## >```
def function_with_default_arguments( arg1, default_arg2 = 100 ):
    "This is a demonstration for default argument"
    print("Value of arg1: ", arg1)
    print("Value of default_arg2: ", default_arg2)
    return
# End of function code: function_with_default_arguments

# calling function: with both arguments 
function_with_default_arguments( arg1 = 10, default_arg2 = 99 )
# Since we supplied "default_arg2 = 99", this over rides the default value of 100
# OUTPUT:
#    Value of arg1:  10
#    Value of default_arg2:  99

#calling function: with ONLY ONE argument and not supplying the default argument
#The function assumes the value for default_arg2 =100( as specified in function code) 
function_with_default_arguments( arg1 = 11)
# OUTPUT:
#    Value of arg1:  11
#    Value of default_arg2:  100
## >```


## >### Variable Length arguments
## >* Python supports arguments of arbitrary-length (variable length or number of 
## >  arguments If there are more than ONE argument,Then the last parameter can be 
## >  made to accept arbitrary number of parameters in its place), start with "*",
## >  the arbitrary-length parameter is a TUPLE.
## >```
def function_with_one_argument_and_arbitrary_length_arguments(arg1, *arbitrary_arguments_tuple):
    "This is a demonstration of the one fixed and arbitrary arguments"
    print('Value of the first argument: ',arg1)
    v=0
    for c1 in arbitrary_arguments_tuple:
        v+=1
        print('Arbitrary Argument number: ',v,' value: ',c1)
# End of function code:  function_with_one_argument_and_arbitrary_length_arguments


# calling the function "function_with_one_argument_and_arbitrary_length_arguments"
# in this case ONE fixed and FOUR variable length,
function_with_one_argument_and_arbitrary_length_arguments(1, 2, 3, 5, 6)

# in this case ONE fixed and FOUR variable length, Same function name
function_with_one_argument_and_arbitrary_length_arguments(1, 'a1', 'a2', 'a3', 'a4', 'a5', 'a6')


# Another function with multiple arguments
def print_all_args(*args):
    for x in enumerate(args):
        print(x)

print_all_args(1,2,3,4,5)

print_all_args('a','b','c','d')

## >```


