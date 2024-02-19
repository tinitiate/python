# addition_module_caller.py
import addition_module

# Using the function from the module with default values
result_default = addition_module.add_variables()
print(f"Default sum is: {result_default}")

# Using the function from the module with custom values
value3 = 5
value4 = 3
result_custom = addition_module.add_variables(value3, value4)
print(f"Custom sum is: {result_custom}")