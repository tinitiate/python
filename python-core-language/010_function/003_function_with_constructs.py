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