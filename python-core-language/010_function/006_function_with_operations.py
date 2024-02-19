def extract_tuple_into_strings_and_numbers(in_tuple):
    "This is a function separates tuple into a stringlist and numberlist based on split type"

    # Store Numbers from "in_list" parameter in number_list
    number_list = []
    
    # Store Strings from "in_list" parameter in string_list
    string_list = []

    work_list = list(in_tuple)

    for c in work_list:
        if c.isdigit():
            number_list.append(c)
        else:
            string_list.append(c)

    # Print Number List
    print(number_list)

    # Print String List
    print(string_list)

# End of function code


# Calling the function extract_tuple_into_strings_and_numbers

# Passing string "number" as the split parameter
extract_tuple_into_strings_and_numbers(('1','A', '2', '3','B', 'c'))

# Passing string "string" as the split parameter
extract_tuple_into_strings_and_numbers(('1','A', '2', '3','B', 'c'))

#OUTPUT:
#       ['1', '2', '3']
#       ['A', 'B', 'c']