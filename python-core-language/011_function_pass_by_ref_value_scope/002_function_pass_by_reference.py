# Create a source list
source_list = ['A', 'B', 'C']

def function_pass_by_reference(in_list):
    print('function_pass_by_reference says Input List: ', in_list)

    # Changing the input by appending a value to in_list
    in_list.append('D')
    print('function_pass_by_reference says changed List: ', in_list)
# End of function code:  function_pass_by_reference

print('Before passing reference to function, source_list: ', source_list)

# Passing the "source_list" and NOT A COPY of the "source_list"
function_pass_by_reference(source_list)
print('After passing reference to function, source_list: ', source_list)

# OUTPUT
#    Before passing to function, source_list:  ['A', 'B', 'C']
#    Input List:  ['A', 'B', 'C']
#    changed List:  ['A', 'B', 'C', 'D']
#    After passing to function, source_list:  ['A', 'B', 'C', 'D']