![Tinitiate Python Training](../images/python-tinitiate.png)
# Object Oriented Programming Vs Functional Programming
* To understand the difference between functional code and Object Oriented programming code, Lets consider a single problem and write code in both functional and Object Oriented Code.
* We demonstrate why Object Oriented Programming is more efficient than Functional Programming for a same problem-solution

## Create a functional code the same as Class
* Lets create a file with functional code, 
```python
n1 = None
n2 = None
        
def add1():
    return n1 + n2

def mul1():
    return n1 * n2
```

## Import Functional Code File
* Here we import the Functionl code file and assign the same values as in 
  the Object Oriented Programming.
* Assigning the values in the functional code caller, and get the function instance size.
```python
import func_test as f1
import func_test as f2

# Create Obj1 of class OOP
f1.num1 = 100
f1.num2 = 200
f1.add1(N1=100, N2=200)
f1.mul1(N1=200, N2=300)
f1.print_class_vars()

# Create Obj2 of class OOP
f2.num1 = 1000
f2.num2 = 2000
f2.add1(N1=400, N2=500)
f2.mul1(N1=600, N2=700)
f2.print_class_vars()

# Print the Object Sizes of both objects
print(f1.__sizeof__() + f2.__sizeof__())
```

## Create a Class
* Here we create a Class (Object Oriented Programming code) with the same functionality of the functional code.
```python
class OOP:

    # Class Variables
    num1 = None
    num2 = None
            
    # Class Methods(Functions)
    def add1(self, N1, N2):
        return N1 + N2

    def mul1(self, N1, N2):
        return N1 * N2

    def print_class_vars(self):
        print("Class OOPs vars:")
        print("num1",self.num1)
        print("num2",self.num2)
```

## Create the Class Object
* Here we create TWO class objects and display the size of each object
```python
from class_test import OOP as t1

# Create Obj1 of class OOP
Obj1 = t1()
Obj1.num1 = 100
Obj1.num2 = 200
Obj1.add1(N1=100, N2=200)
Obj1.mul1(N1=200, N2=300)
Obj1.print_class_vars()

# Create Obj2 of class OOP
Obj2 = t1()
Obj2.num1 = 1000
Obj2.num2 = 2000
Obj2.add1(N1=400, N2=500)
Obj2.mul1(N1=600, N2=700)
Obj2.print_class_vars()

# Print the Object Sizes of both objects
print(Obj1.__sizeof__() + Obj2.__sizeof__())
```

## Python: Functional Code vs. Object-Oriented Code - Pros and Cons
* Python supports both functional programming and object-oriented programming paradigms, offering developers the flexibility to choose the approach that best fits their needs.
* Each paradigm has its own set of pros and cons, and the choice between functional and object-oriented code often depends on the specific requirements of the project and the developer's preferences. 

### Functional Programming
* Pros:
  * **Simplicity and Readability:** Functional code tends to be concise and expressive, making it easier to read and understand.
  * Emphasis on pure functions, which have no side effects, leads to code that is easier to reason about.
  * **Immutability:** Immutable data structures prevent unexpected changes to data, promoting safer and more predictable code.
  * Avoiding mutable state simplifies debugging and makes the code more thread-safe.
  * **Parallelism and Concurrency:** Pure functions are inherently thread-safe, facilitating parallelism and concurrency.
  * Functions that don't rely on shared state can be easily parallelized.
  * **Easy Testing:** Pure functions make unit testing straightforward since they have no dependencies on external state.
* Cons:
  * **Learning Curve:** Functional programming concepts, such as higher-order functions and immutability, may have a steeper learning curve for developers accustomed to imperative programming.
  * **Performance Overhead:** Immutable data structures and functional constructs might introduce a performance overhead compared to their mutable counterparts.
  * **Limited Tooling for Certain Domains:** In some domains, such as GUI programming, functional programming might not have as mature tooling or standard practices.

### Object-Oriented Programming (OOP)
* Pros:
  * **Modularity and Reusability:** OOP encourages the creation of modular and reusable code through encapsulation, inheritance, and polymorphism.
Classes provide a natural way to structure and organize code.
  * **Abstraction:** Abstraction allows developers to focus on high-level functionality without worrying about implementation details.
Well-designed class hierarchies provide a clear structure for the application.
  * **Readability and Maintainability:** OOP code can be more readable and maintainable, especially for large and complex systems.
  * Encapsulation hides internal details, reducing complexity.
  * **Widely Used in Industry:** Many large-scale software projects and frameworks are built using OOP principles, making it a valuable skill for developers entering the industry.
* Cons:
  * **Boilerplate Code:** OOP code can sometimes involve more boilerplate code, leading to verbosity.
  * Inheritance hierarchies can become overly complex and introduce maintenance challenges.
  * **Mutable State:** Encapsulation doesn't guarantee immutability, and mutable state can lead to unexpected side effects.
  * Managing state can be challenging, especially in concurrent environments.
  * **Performance Concerns:** Some OOP constructs might introduce performance overhead, and optimizing OOP code can be more complex.

### Conclusion
* The choice between functional and object-oriented programming in Python depends on the specific requirements of the project, the preferences of the development team, and the nature of the problem domain.
* In many cases, a hybrid approach that combines elements of both paradigms can provide a balanced solution, leveraging the strengths of each to create robust and maintainable code.
* Developers should carefully consider the trade-offs and choose the paradigm that aligns best with the goals of their project.


* * *
| (c) TINITIATE / Venkata Bhattaram |
| :--- |