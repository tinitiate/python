# Create a source list
source_list_2 = ['A', 'B', 'C']

def function_pass_by_value(in_list):
    print('function_pass_by_value says Input List: ', in_list)

    # Reassigning a local value, [pass by value example]
    in_list =[1, 2, 3, 4]
    print('function_pass_by_value says changed List: ', in_list)
# End of function code:  function_pass_by_value


print('Before passing by value to function, source_list: ', source_list_2)

# Passing the "source_list" and NOT A COPY of the "source_list"
function_pass_by_value(source_list_2)
print('After passing by value to function, source_list: ', source_list_2)

# OUTPUT
#    Before passing to function, source_list:  ['A', 'B', 'C']
#    Input List:  ['A', 'B', 'C']
#    changed List:  ['A', 'B', 'C', 'D']
#    After passing to function, source_list:  ['A', 'B', 'C', 'D']