# What is print() in Python?

* In Python, print() is a built-in function that is used to output information to the console or terminal. It allows you to display text, variables, and other data in a human-readable format. The print() function takes one or more arguments, which are the values you want to display, and it separates them with a space by default.
```python
# Example: Displaying Text
print("Hello, world!")
# Example: Displaying Variables
name = "Alice"
age = 30
print("Name:", name, "Age:", age)
```
* You can customize the way `print()` outputs data using various parameters. For example, you can use the sep parameter to change the separator between multiple arguments:

```python
Print("apple", "banana", "orange", sep=", ")
```
* Additionally, you can use the end parameter to specify what character(s) should be printed at the end of the print() statement, instead of the default newline character:

```
print("Hello", end=" ")
print("World")
```
* These are just a few examples of how you can use the print() function in Python to display information. It's a fundamental tool for debugging, logging, and interacting with users through the console.
