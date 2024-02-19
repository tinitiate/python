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