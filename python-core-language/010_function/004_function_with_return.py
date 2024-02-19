"""
def return_sum(num1, num2):
    return num1+num2
    print(123)

## Call the function
## Store the value to a variable
x = return_sum(1, 2)
print(x)

## Call the function, Use the call in a print
print(return_sum(1, 2))

x = return_sum(return_sum(1, 2), return_sum(1, 2))
print(x)
x = return_sum(num1=return_sum(1, 2), num2=return_sum(1, 2))
print(x)

"""
def even_odd(num1):
    if num1%2 == 0:
        return "Even"
        print(11)
    else:
        return "Odd"
        return "a"
        print(22)

print(even_odd(11))
print(even_odd(12))
