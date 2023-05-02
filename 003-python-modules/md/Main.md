# Main()

* The `main()` function is a special function in Python that serves as the entry point of a program. 

* It is the function that is executed when the program is run. 

* The `main()` function typically contains the top-level logic of the program, including the initialization of variables, the invocation of other functions, and the handling of any exceptions that might occur.

* In Python, the `main()` function is often implemented using a conditional statement that checks whether the current module is being run as the main program. 

  * This is done using the `if __name__ == "__main__":` statement.

  * If this condition is true, then the code within the block following the statement is executed.

    ```python
    def main():
        print("Hello, world!")
    
    if __name__ == "__main__":
        main()
    
    ```

  * While it is common to name the entry point function in a Python program `main()`, it is not strictly required.

  * We can name the entry point function whatever you like, as long as you indicate it as the entry point using the `if __name__ == "__main__":` statement.

    ```python
    def start():
        # Initialization code goes here
        print("Starting program...")
        # Main program logic goes here
    
    if __name__ == "__main__":
        start()
    
    ```

##  `if __name__ == "__main__"`

* The `if __name__ == "__main__"` statement is a special statement in Python that is used to control the execution of code. 

* When the `if __name__ == "__main__"` statement is executed, the code inside the `if` block will only be executed if the script is being run as the main program.

* If the script is being imported as a module, the code inside the `if` block will not be executed.

* If the script is imported as a module, the `main()` function will not be called and no output will be displayed.

* The `if __name__ == "__main__"` statement is a powerful tool that can be used to control the execution of code in Python scripts.

  ```python
  # math_functions.py
  
  import math
  
  def square_root(n):
      return math.sqrt(n)
  
  def main():
      n = float(input("Enter a number: "))
      result = square_root(n)
      print("The square root of", n, "is", result)
  
  if __name__ == "__main__":
      main()
  
  ```

  ```python
  # my_program.py
  
  from math_functions import square_root
  
  n = 16
  result = square_root(n)
  print("The square root of", n, "is", result)
  
  ```

* In this case, the `if __name__ == "__main__":` statement in `math_functions.py` prevents the code in the `main()` function from executing when the module is imported into `my_program.py`. This ensures that the user input prompt and output statements in `main()` are not executed when the `square_root()` function is imported and used in another program.

* Instead, only the code within the `square_root()` function is executed when it is called from `my_program.py`, and the user input and output statements in `main()` are not executed. This allows you to reuse the `square_root()` function without executing the entry point function when it is not intended to be run.

  ```python
  # math_functions.py
  
  import math
  
  def square_root(n):
      return math.sqrt(n)
  
  def power(x, n):
      return x ** n
  
  def main():
      n = float(input("Enter a number: "))
      x = float(input("Enter a power: "))
      result1 = square_root(n)
      result2 = power(x, n)
      print("The square root of", n, "is", result1)
      print(x, "raised to the power of", n, "is", result2)
  
  if __name__ == "__main__":
      main()
  
  ```

  ```python
  # my_program.py
  
  from math_functions import square_root, power
  
  n = 16
  x = 2
  result1 = square_root(n)
  result2 = power(x, n)
  print("The square root of", n, "is", result1)
  print(x, "raised to the power of", n, "is", result2)
  
  ```

* In this example, the `square_root()` and `power()` functions from `math_functions.py` are imported into `my_program.py` using the `from math_functions import square_root, power` statement. The functions are then called to perform their respective operations on the input values, and the results are printed to the console.

* In this way, the `if __name__ == "__main__":` statement in `math_functions.py` ensures that the user input prompt and output statements in the `main()` function are not executed when the module is imported into `my_program.py`, and only the definitions of the `square_root()` and `power()` functions are imported and used.

* Example of what can happen if you don't use the `if __name__ == "__main__":` statement in your main program:

* ```python
  # math_functions.py
  
  import math
  
  def square_root(n):
      return math.sqrt(n)
  
  def power(x, n):
      return x ** n
  
  def main():
      n = float(input("Enter a number: "))
      x = float(input("Enter a power: "))
      result1 = square_root(n)
      result2 = power(x, n)
      print("The square root of", n, "is", result1)
      print(x, "raised to the power of", n, "is", result2)
  
  main()
  
  ```

  ```python
  # my_program.py
  
  from math_functions import square_root, power
  
  n = 16
  x = 2
  result1 = square_root(n)
  result2 = power(x, n)
  print("The square root of", n, "is", result1)
  print(x, "raised to the power of", n, "is", result2)
  
  ```

* In this example, when you run `my_program.py`, the `main()` function in `math_functions.py` will be executed, and the user input prompt and output statements will be printed to the console, even though they are not relevant to `my_program.py`. 

* To avoid this issue, it's a good practice to always use the `if __name__ == "__main__":` statement in your main program, as shown in the previous examples, to ensure that the entry point code is only executed when the module is run as the main program, and not when it is imported as a module into another program.

