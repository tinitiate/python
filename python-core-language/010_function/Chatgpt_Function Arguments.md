Function Arguments in Python

In Python, function arguments are the values that you provide to a function when you call it. They allow you to pass data to a function so that it can perform its tasks using that data. Function arguments enable you to make your functions more versatile and capable of handling different inputs.

Types of Function Arguments
Positional Arguments: These are the most basic type of arguments. They are passed to a function in the order they are defined in the function's parameter list.
Keyword Arguments: With keyword arguments, you explicitly mention the parameter name along with the value when calling the function. This allows you to pass arguments in any order and makes the code more readable.
Default Arguments: Default arguments are assigned default values in the function's parameter list. If you don't provide a value for these arguments when calling the function, the default value is used.
Variable-Length Arguments:
Arbitrary Positional Arguments (*args): This allows you to pass a variable number of positional arguments to a function. The arguments are collected into a tuple.
**Arbitrary Keyword Arguments (kwargs): Similar to args, this allows you to pass a variable number of keyword arguments to a function. The arguments are collected into a dictionary.
Example
python
Copy code
# Positional Arguments
def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")

greet("Alice", 30)  # Positional arguments passed in order

# Keyword Arguments
greet(age=25, name="Bob")  # Keyword arguments, order doesn't matter

# Default Arguments
def power(base, exponent=2):
    result = base ** exponent
    print(f"{base} raised to the power of {exponent} is {result}")

power(3)      # Uses default exponent (2)
power(2, 4)   # Overrides default exponent

# Variable-Length Arguments
def show_items(*items):
    print("Items:")
    for item in items:
        print(item)

show_items("apple", "banana", "cherry")

def show_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=30, city="Wonderland")
In the above example, we've demonstrated different types of function arguments. Understanding and using these argument types allows you to create functions that are flexible and cater to various scenarios.