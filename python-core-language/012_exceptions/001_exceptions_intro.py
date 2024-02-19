print("Start")
# a=1/0
# We attempt to divide by zero, raising an exception
try:
    print(1)
    v = 1/1  # Trying to Divide By zero
except ZeroDivisionError:              # EXCEPTION HANDLER1
    print("Tinitiate: Cannot Divide by ZERO")
# except:                                # EXCEPTION HANDLER2
#     print("Some Other Exception")
except Exception as e:                 # EXCEPTION HANDLER2 (With Name and Error Message)
    print(type(e).__name__, e)
else:
    print("Tinitiate: Execution completed successfully")

print("End")
# print(a) # = Exceptions = Runtime Errors
# print(a = ERROR
      