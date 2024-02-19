def function_with_regular_arguments(arg1, arg2):
    print(arg1+arg2)
# End of function code: function_with_regular_arguments

# Calling the function function_with_regular_arguments
# positional param call of function
function_with_regular_arguments('Pyt','hon')
# OUTPUT: Python

function_with_regular_arguments('hon','pyt')
# OUTPUT: honpyt
# Order if supplying arguments matters in the regular call, since the calls are 
# made by position of the arguments

# named param call of function
function_with_regular_arguments(arg2='hon', arg1='pyt')
# OUTPUT: Python