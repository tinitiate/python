def function_with_default_arguments( arg1, default_arg2 = 100 ):
    "This is a demonstration for default argument"
    print("Value of arg1: ", arg1)
    print("Value of default_arg2: ", default_arg2)
# End of function code: function_with_default_arguments

# calling function: with both arguments 
function_with_default_arguments( arg1 = 10, default_arg2 = 99 )
function_with_default_arguments(10,99)

# Since we supplied "default_arg2 = 99", this over rides the default value of 100
# OUTPUT:
#    Value of arg1:  10
#    Value of default_arg2:  99

#calling function: with ONLY ONE argument and not supplying the default argument
#The function assumes the value for default_arg2 =100( as specified in function code) 
function_with_default_arguments( arg1 = 11)
function_with_default_arguments(11)
# OUTPUT:
#    Value of arg1:  11
#    Value of default_arg2:  100