def extract_dictionary_keys_values(in_dictionary):
    "This is a function separates dictionary KEYS and VALUES into lists and prints them"
    
    # Print Keys, Using the ".KEYS" and enclosed in the "list()" function
    print(list(in_dictionary.keys()))

    # Print Keys, Using the ".VALUES" and enclosed in the "list()" function
    print(list(in_dictionary.values()))

# End of function code

# Calling the function extract_dictionary_keys_values
extract_dictionary_keys_values({1:'A',2:'B', 3:'C'})

#OUTPUT:
#       ['1', '2', '3']
#       ['A', 'B', 'c']