# __main__.py
from math_module import add_variables
from multiplication_module import multiply_variables

def main():
    # Using the add_variables function from math_module
    value1 = int(input("Enter the first number for addition: "))
    value2 = int(input("Enter the second number for addition: "))
    result_add = add_variables(value1, value2)
    print(f"The sum is: {result_add}")

    # Using the multiply_variables function from multiplication_module
    value3 = int(input("Enter the first number for multiplication: "))
    value4 = int(input("Enter the second number for multiplication: "))
    result_multiply = multiply_variables(value3, value4)
    print(f"The product is: {result_multiply}")

if __name__ == "__main__":
    # This block will only execute if this script (__main__.py) is run directly.
    main()