Pass By Reference, Variable Scope, and Function Behavior in Python

Pass By Reference vs. Pass By Value
Python uses a mechanism often referred to as "pass by reference of the value." This can lead to confusion because it behaves differently from traditional "pass by reference" and "pass by value" terminologies.

Pass By Value: A copy of the value is passed to the function. Changes to the function parameter do not affect the original variable.
Pass By Reference: A reference to the original variable is passed. Changes to the function parameter affect the original variable.
In Python, when you pass an immutable object (like numbers, strings, tuples) to a function, it behaves like pass by value. Changes inside the function do not affect the original object. When you pass a mutable object (like lists, dictionaries) to a function, it behaves like pass by reference. Changes inside the function can affect the original object.

Variable Scope
In Python, the scope of a variable defines where the variable is accessible and can be manipulated. There are mainly two types of variable scope:

Local Scope: Variables declared within a function are considered to have a local scope. They are only accessible within that function.
Global Scope: Variables declared outside of any function are considered to have a global scope. They are accessible throughout the entire script/module.
Example
python
Copy code
# Pass By Reference Example
def modify_list(lst):
    lst.append(4)  # Modifying the list inside the function

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

# Pass By Value Example
def modify_number(num):
    num = num + 1  # Modifying the number inside the function

my_num = 5
modify_number(my_num)
print(my_num)  # Output: 5

# Variable Scope Example
global_variable = 10  # Global variable

def func():
    local_variable = 20  # Local variable
    print(global_variable)  # Accessing global variable inside function
    print(local_variable)

func()
print(global_variable)  # Accessing global variable outside function
#print(local_variable)  # This line would raise an error
In the provided examples:

modify_list function modifies the list passed to it, reflecting changes globally.
modify_number function doesn't affect the original number since it's immutable.
The func function demonstrates variable scope, where global_variable is accessible both inside and outside the function, while local_variable is only accessible inside the function.