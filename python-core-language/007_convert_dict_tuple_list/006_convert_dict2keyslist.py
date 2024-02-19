# Convert DICTIONARY to LIST of elements
list_tup = [(1, 'A'), (2, 'B'), (3, 'C')]
finalDictionaryBigList=[]

# Loop through the dict_list to create individual tuples
for tuples in list_tup: 
    #Capture individual tuples
    IndividualTuple = tuples
    #Convert individual tuples to lists
    IndividualTuplesList = list(IndividualTuple)
    # Append the IndividualTuplesList to a final List
    finalDictionaryBigList = finalDictionaryBigList + IndividualTuplesList

# Print the final flat list from the dictionary
print(finalDictionaryBigList)