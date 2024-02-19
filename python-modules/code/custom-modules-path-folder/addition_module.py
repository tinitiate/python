# addition_module.py
def add_variables(var1=0, var2=0):
    """Add two variables and return the result."""
    return var1 + var2

if __name__ == "__main__":
    # This block of code will only run if this script is executed directly
    # and not when it's imported as a module.
    
    # You can use this block to test the functionality if needed.
    value1 = int(input("Enter the first number: "))
    value2 = int(input("Enter the second number: "))
    
    result = add_variables(value1, value2)
    print(f"The sum is: {result}")