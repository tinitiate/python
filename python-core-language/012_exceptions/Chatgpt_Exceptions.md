Exceptions in Python

In Python, exceptions are events that occur during the execution of a program that disrupt the normal flow of the program's instructions. They usually arise due to errors or exceptional conditions that the programmer might not have anticipated. Python provides a robust mechanism for handling exceptions, allowing you to gracefully manage errors and prevent your program from crashing unexpectedly.

Exception Hierarchy
Python's exception system is organized in a hierarchy, with a base BaseException class at the top. Different types of exceptions are derived from this base class, forming a tree-like structure. This hierarchy allows you to catch specific exceptions while still being able to catch more general ones if needed.

Handling Exceptions
To handle exceptions, you use try and except blocks. The try block contains the code that might raise an exception, and the except block catches and handles the exception if it occurs.

python
Copy code
try:
    # Code that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Code to handle the exception
    print("Division by zero is not allowed.")
In this example, the try block attempts to perform a division by zero, which raises a ZeroDivisionError exception. The except block catches this exception and provides an appropriate error message.

Handling Multiple Exceptions
You can handle multiple exceptions by specifying multiple except blocks or using a single except block that handles a tuple of exception types.

python
Copy code
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")
The else and finally Clauses
The else block is executed when no exceptions are raised in the try block. It's often used to place code that should run only if the try block completes successfully.
The finally block contains code that is executed no matter what, whether an exception occurred or not. It's used for cleanup operations, like closing files or releasing resources.
python
Copy code
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete.")
Custom Exceptions
You can also create custom exception classes by subclassing built-in exception classes. This is useful when you want to raise exceptions specific to your program's logic.

python
Copy code
class CustomError(Exception):
    pass

def process_data(data):
    if not data:
        raise CustomError("No data provided!")

try:
    process_data(None)
except CustomError as ce:
    print(ce)
In this example, a custom exception class CustomError is defined, and a function process_data raises it when no data is provided.

