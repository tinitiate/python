Iterative Loops in Python

Iterative loops in Python are programming constructs that allow you to repeat a set of instructions multiple times. They enable you to automate repetitive tasks, iterate through data structures, and perform actions based on specific conditions. Python provides two primary types of loops: the for loop and the while loop.

The for Loop
The for loop iterates over a sequence (like a list, tuple, or string) and executes a block of code for each item in the sequence:

python
Copy code
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")
You can also use the range() function to generate a sequence of numbers to iterate over:

python
Copy code
for i in range(5):
    print(i)
The while Loop
The while loop repeatedly executes a block of code as long as a specified condition is true:

python
Copy code
count = 0
while count < 5:
    print(count)
    count += 1
Be cautious when using while loops to avoid infinite loops—loops that never terminate if the condition is never met.

Loop Control Statements
Python provides loop control statements to modify the behavior of loops:

break: Terminates the loop prematurely.
continue: Skips the current iteration and proceeds to the next one.
else: Executes a block of code after the loop finishes, but only if the loop was not terminated by a break statement.
Iterating with Index
To iterate through both the elements and their indices in a sequence, you can use the enumerate() function:

python
Copy code
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
Nested Loops
You can nest loops within other loops to create complex iterations:

python
Copy code
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
Conclusion
Iterative loops are essential programming constructs that allow you to execute repetitive tasks efficiently in Python. Whether you're working with sequences, numbers, or conditions, loops provide the means to automate operations and control the flow of your program