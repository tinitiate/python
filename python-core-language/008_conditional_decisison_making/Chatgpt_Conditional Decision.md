# Conditional Decision Making in Python

* Conditional decision making in Python refers to the process of making choices in your code based on certain conditions. It allows your program to execute different code blocks depending on whether specific conditions are satisfied or not.
* Python provides various ways to implement conditional decision making using if statements, elif statements, and else statements.

## The if Statement
* The if statement is used to execute a block of code only if a specified condition is true:
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

## The if-else Statement
* The if-else statement allows you to execute one block of code if a condition is true and another block if the condition is false:
```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

## The if-elif-else Statement
* The if-elif-else statement lets you check multiple conditions in a sequence and execute different blocks of code based on the first true condition:
```python
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but not greater than 10")
else:
    print("x is 5 or less")
```

## Logical Operators
* You can combine conditions using logical operators: and, or, and not:
```python
x = 8
if x > 5 and x < 10:
    print("x is between 5 and 10")
```

## Nested if Statements
* You can nest if statements within other if statements to create more complex decision structures:
```python
x = 5
if x > 0:
    if x % 2 == 0:
        print("x is a positive even number")
    else:
        print("x is a positive odd number")
else:
    print("x is not a positive number")
```

## Ternary Conditional Operator
* Python also offers a ternary conditional operator for concise single-line conditionals:
```python
x = 7
result = "greater than 5" if x > 5 else "not greater than 5"
print(result)
```

* Conditional decision making in Python allows you to control the flow of your program based on specific conditions. 
* By using if, elif, else statements, logical operators, and nested structures, you can create versatile and responsive programs that execute different code paths as needed.