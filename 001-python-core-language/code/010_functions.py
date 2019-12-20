## >---
## >YamlDesc: CONTENT-ARTICLE
## >Title: python functions
## >MetaDescription: python functions, function with parameters, function with return value example code, tutorials
## >MetaKeywords: python functions, function with parameters, function with return value example code, tutorials
## >Author: Venkata Bhattaram / tinitiate.com
## >ContentName: functions
## >---

## ># PYTHON FUNCTIONS
## >* Function is a code block, that can be called once or multiple times.
## >  Functions can be reused and provide code modularity, they can accept 
## >  input parameters to be used with in its code body.
## >* In Python create functions using keyword "def" function-name  
## >  def myFunction myFunction and parameters(or arguments) in curved  
## >  brackets def myFunction(): and a colon to end :
## >* Code inside the function must be indented, meaning all code inside a 
## >  function must atleast have 2 spaces in front of them, Any code with out 
## >  that indentation means that code is outside the function code.
## >* An optional indented first line can be used to add a Documentation String,
## >  a brief one liner to describe the function's functionality and parameters.

## >* Sample function syntax without arguments def myFunctionName():
## >* Sample function syntax with one argument def myFunctionName(input):
## >* Sample function syntax with multiple arguments 
## >  def myFunctionName(input1, input2):
## >* Note that python interpreter looks for code indentation make sure     
## >  next line is indented by atleast 1 whitespace.
## >* Loops in functions and if..else in functions
## >* sample usage of List with functions, Tuple with function, 
## >  Dictionary with function


## >### Python Function Example
## >```
# Step 1 Create a Function
# Here we Create a function called "myFunc" using the 'def' keyword
def myFunc():
   # Code is indented, notice the spacing
   # This is the documentation string
   "This is a function without any input values or return values"
   # Code content
   print("This message is from the function: myFunc")
# End of function code: myFunc

# Step 2.
# Calling the function (Can be called as many times as needed)
# By calling the function, the function executes
myFunc()

# Calling the function again
myFunc()

#OUTPUT:
#    This message is from the function: function_no_input_args_no_return
#    This message is from the function: function_no_input_args_no_return
## >```


## >### Python Function with input parameters and a return value
## >* Input parameters are values that can be passed to the function
## >* Also the parameters can be used inside the functions as values, 
## >  Meaning they can only be used but not assigned values.
## >```
def Add2Nums(number1, number2):
    "This is a function with 2 input parameters and returning the sum"
    print('Sum of',number1,'and',number2,'is',number1+number2)
# End of function code: Add2Nums

# Calling the function with input parameters
Add2Nums(1,2)  # These are the input parameters
Add2Nums(10,20)

# OUTPUT:
# This message is from the function: myFunc
# This message is from the function: myFunc
# Sum of 1 and 2 is 3
# Sum of 10 and 20 is 30
## >```



## >### Python Function with loop and conditional constructs
## >* This function code has constructs of IF ELSE condition and
## >  LOOP constructs.
## >```
def function_with_constructs(in_string, in_number):
    "This function demonstrates use of various built-in constructs"

    # 1. Demonstration of Loop inside a function
    #    Here we print the parameter in_string 5 times
    for c in range(5):
        print(in_string)

    # 2. Demonstration of IF condition inside the function
    #    Here we check if the parameter in_number is even or odd
    if in_number%2 == 0:
        print(in_number,' is even.')
    elif in_number%2 != 0:
        print(in_number,' is odd.')
# End of function code: function_with_constructs

# Calling the function function_with_constructs
function_with_constructs("Python", 20)
#OUTPUT:
#    Python
#    Python
#    Python
#    Python
#    Python
#    20  is even.
## >```


## >### Python Function with Retrun Value
## >* A function can **RETURN** a value, Which is a value is substituted in the 
## >  place of the function call.
## >* The function when returns a value, Must be stored in a variable,
## >* OR the function can be put in a print statement if the return value is
## >  printable.
## >```
def return_sum(num1, num2):
    return num1+num2

## Call the function
## Store the value to a variable
x = return_sum(1, 2)
print(x)

## Call the function, Use the call in a print
print(return_sum(1, 2))
## >```


## >### Python Function with a LIST input parameter
## >* This function **EXTRACT_LIST_INTO_STRINGS_AND_NUMBERS** accepts a List as 
## >  input parameter
## >* This function seperates Numbers and Alphabets and prints them
## >```
def extract_list_into_strings_and_numbers(in_list):
    "This is a function separates list into a stringlist and numberlist"
    
    # Store Numbers from "in_list" parameter in number_list
    number_list = []
    
    # Store Strings from "in_list" parameter in string_list
    string_list = []

    # Loop through the input parameter list
    for c in in_list:
        if c.isdigit():
            number_list.append(c)
        else:
            string_list.append(c)

    # Print Number List
    print(number_list)

    # Print String List
    print(string_list)

# End of function code


# Calling the function extract_list_into_strings_and_numbers
# Passing number as the split parameter
extract_list_into_strings_and_numbers(['1','A', '2', '3','B', 'c'])

# OUTPUT:
#        ['1', '2', '3']
#        ['A', 'B', 'c']
## >```


## >### Python Function with a TUPLE input parameter
## >* This function **EXTRACT_TUPLE_INTO_STRINGS_AND_NUMBERS** accepts a Tuple
## >  as input parameter
## >* This function seperates Numbers and Alphabets and prints them
## >```
def extract_tuple_into_strings_and_numbers(in_tuple):
    "This is a function separates tuple into a stringlist and numberlist based on split type"

    # Store Numbers from "in_list" parameter in number_list
    number_list = []
    
    # Store Strings from "in_list" parameter in string_list
    string_list = []

    work_list = list(in_tuple)

    for c in work_list:
        if c.isdigit():
            number_list.append(c)
        else:
            string_list.append(c)

    # Print Number List
    print(number_list)

    # Print String List
    print(string_list)

# End of function code


# Calling the function extract_tuple_into_strings_and_numbers

# Passing string "number" as the split parameter
extract_tuple_into_strings_and_numbers(('1','A', '2', '3','B', 'c'))

# Passing string "string" as the split parameter
extract_tuple_into_strings_and_numbers(('1','A', '2', '3','B', 'c'))

#OUTPUT:
#       ['1', '2', '3']
#       ['A', 'B', 'c']
## >```


## >### Python Function with a DICTIONARY input parameter
## >* This function accept a DICTIONARY as input parameter and seperates KEYS 
## >  and VALUES from the input parameter and prints them as LISTS.
## >```
def extract_dictionary_keys_values(in_dictionary):
    "This is a function separates dictionary KEYS and VALUES into lists and prints them"
    
    # Print Keys, Using the ".KEYS" and enclosed in the "list()" function
    print(list(in_dictionary.keys()))

    # Print Keys, Using the ".VALUES" and enclosed in the "list()" function
    print(list(in_dictionary.values()))

# End of function code

# Calling the function extract_dictionary_keys_values
extract_dictionary_keys_values({1:'A',2:'B', 3:'C'})

#OUTPUT:
#       ['1', '2', '3']
#       ['A', 'B', 'c']
## >```
