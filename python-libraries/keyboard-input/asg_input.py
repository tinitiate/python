import sys

def add2nums(n1,n2):
    print(n1+n2)


# Directly Call with values in script
add2nums(n1=100,n2=33)

# Get values using input,
# REMEMBER input data is all STRINGS Convert to the datatypes as needed
in_n1 = int(input("Enter value for n1: "))
in_n2 = int(input("Enter value for n2: "))
add2nums(n1=in_n1,n2=in_n2)


# Get values using input,
# REMEMBER sys.argv LIST data is all STRINGS Convert to the datatypes as needed
inputs = sys.argv
add2nums(n1=int(inputs[1]),n2=int(inputs[2]))


