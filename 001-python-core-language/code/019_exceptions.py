## >---
## >YamlDesc: CONTENT-ARTICLE
## >Title: Python Exceptions
## >MetaDescription: Python Exceptions try, except, else, finally, Custom Exceptions, Multiple Exceptions example code, tutorials
## >MetaKeywords: Python Exceptions try, except, else, finally, Custom Exceptions, Multiple Exceptions example code, tutorials
## >Author: Venkata Bhattaram / tinitiate.com
## >ContentName: exceptions
## >---

## ># Python Exceptions
## >* PYTHON Exceptions, Are RUN TIME ERRORS or EXECUTION TIME ERRORS
## >* CODE that doesn't handle exceptions will compile, but when the un-handled 
## >  exception is encountered then the program exits at the point of failure.
## >* Handling exceptions in PYTHON is done using
## >  "try: ... except ... finally" block
## >* providing an ELSE with try: block 
## >* Using PYTHON finally to execute code, irrespective of try-block raising
## >  an exception.
## >* PYTHON Custom user defined exceptions and exception handler
## >* PYTHON, single try can have multiple exception handlers
## >* PYTHON ignore exception, use pass keyword in the except section

## >## Python Exception Example
## >```
# We attempt to divide by zero, raising an exception
try:
    v = 1/0  # Trying to Divide By zero
except ZeroDivisionError:
    print("Tinitiate: Cannot Divide by ZERO")
## >```


## >## PYTHON Exception using ELSE Example
## >* Using "else:" to complete normal execution and subsequent code in a try block
## >* We attempt to divide by zero, raising an exception
## >```
try:
    v = 1/1  # Trying to Divide By zero
except ZeroDivisionError:
    print("Tinitiate: Cannot Divide by ZERO")
else:
    print("Tinitiate: Execution completed successfully")
## >```


## >## PYTHON Exception using FINALLY Example
## >* The finally block executes, whether the irrespective of try-block 
## >* raising an exception, This is useful to put code/functions 
## >  where such scenarios are needed
## >```
try:
    v = 1/1  # Trying to Divide By zero
except ZeroDivisionError:
    print("Tinitiate: Cannot Divide by ZERO")
finally:
    print("Tinitiate: THIS MESSAGE MUST BE PRINTED")
## >```


## >## PYTHON User defined Exceptions
## >```
# Create an user defined exception
class tinitiate_exception(Exception):pass

# Block to test the user defined exception
try:
    raise tinitiate_exception
except tinitiate_exception:
    print("This is a user defined exception !")
## >```


## >## PYTHON Multiple Exceptions in a single try
## >```
# Creating USER defined exceptions
class ti_exception_1(Exception):pass
class ti_exception_2(Exception):pass

# Block to test the user defined exception
try:
    raise ti_exception_1
except ti_exception_1: # Exception handler for user defined exception: ti_exception_1
    print("This is a user defined exception 1 Handler !")
except ti_exception_2: # Exception handler for user defined exception: ti_exception_2 
    print("This is a user defined exception 2 Handler !")
## >```


## >## Python Perform no action on exception example
## >* Using **pass** in the **except** block will take no action, when an
## >*  EXCEPTION is encountered.
## >```
try:
    a=1/0
except:
    pass  # This will do nothing
## >```

## >## Python Default Exception
## >* Get Exception Name and Message
## >```
try:
    v = 1/0
except Exception as e:
    print(type(e).__name__, e)
## >```    


