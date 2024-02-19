"""
def function_with_one_argument_and_arbitrary_length_arguments(arg1, *arbitrary_arguments_tuple):
    "This is a demonstration of the one fixed and arbitrary arguments"
    print('Value of the first argument: ',arg1)
    v=0
    for c1 in arbitrary_arguments_tuple:
        v+=1
        print('Arbitrary Argument number: ',v,' value: ',c1)
# End of function code:  function_with_one_argument_and_arbitrary_length_arguments

# calling the function "function_with_one_argument_and_arbitrary_length_arguments"
# in this case ONE fixed and FOUR variable length,
function_with_one_argument_and_arbitrary_length_arguments(1, 2, 3, 5, 6)

# in this case ONE fixed and FOUR variable length, Same function name
function_with_one_argument_and_arbitrary_length_arguments(1, 'a1', 'a2', 'a3', 'a4', 'a5', 'a6')

# Another function with multiple arguments
def print_all_args(*args):
    for x in args:
        print(x)

# print_all_args(1,2,3,4,5)
# print_all_args(1,2,3,4)
# print_all_args(1,2,3)
print_all_args('a',1,22.33,'d')
"""

def greatest(*n):
    print(max(n))

greatest(1,33,55,111,2)
greatest(100,33)
greatest(-1,3,30,33)