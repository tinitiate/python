![Tinitiate Python Training](../images/python-tinitiate.png)
# Python Object-Oriented Programming (OOP)
* Object-Oriented Programming (OOP) is a programming paradigm that uses objects to organize code.
* Python, a versatile and powerful programming language, supports OOP principles, making it easy to create modular and reusable code.

## Classes
* Python supports, Object Oriented Programming, Its a concept where data and
  functionality are combined into a unit called as CLASS.
* Class is a collection of DATA and FUNCTIONS that operate on that data
* Data could be **Class Variables** (or CLASS ATTRIBUTES) Lists, tuples, dictionaries.
* **Methods or Functions** are operations that perform operations on data values, such as get squareroot or get square of a given data set.
* For more complex business scenarios, Data could be Credit and salary
  information and the function could be approve/disapprove loan.
* Objects are instantiation of classes (reference of a class instance)
* While Class is a Spefcification, Object is the implementation 
  (or the executing instance of the class).
* **Class** is a blueprint for creating objects. **Objects** are instances of a class, and each object can have attributes (characteristics) and methods (functions).

## Objects
* To use or run a **class** we need to create an **Object**.
* An object is a runtime instance of a class, and a class is a blueprint for creating objects.
* In other words, an object is a self-contained unit that consists of data and associated methods that operate on that data.
* Objects in Python can represent real-world entities, such as a person, a car, or an abstract concept like a file or a network connection.
* Instances of Classes: Objects are instances of classes. A class defines the properties (attributes) and behaviors (methods) that its objects will have.
```python
##################
# Create a CLASS #
##################
class Tinitiate:
    'This is a brief note about the class, This is the TINITIATE Class'
    
    # CLASS VARIABLES / ATTRIBUTES
    # a class Variable
    ti_var   = 100
    # a class list
    ti_list  = ["a","b","c"]
    # a class tuple
    ti_tuple = ("x","y","z")
    # a class dictionary
    ti_dictionary = {"1":"A", "2":"b", "3":"c"}

    # CLASS FUNCTION
    def ti_function(self):
        "This is a class function"
        print("This is a message from the TINITIATE Class ti_function")

#################
# Using a Class #
#################

# Create an object of the class
# This will instantiate the Class
tinObject = Tinitiate()

# use the Class variables/lists..
print(tinObject.ti_var)
print(tinObject.ti_list)
print(tinObject.ti_tuple)
print(tinObject.ti_dictionary)

# Call the the class function
tinObject.ti_function() # This will print the message from the function

# Create another object of the class
tObject = Tinitiate()

# Call the the class function
tObject.ti_function()
```

## Python Class Private variables
* In Python, you can create private variables in a class by prefixing the variable name with two underscores (__). 
* This practice is known as name mangling, and it makes it harder for external code to access the variable directly.
* However, it's important to note that Python does not provide true "private" variables; instead, it offers a way to make it more challenging for external code to access them.
* Here's an example demonstrating private variables in a class:
```python
class MyClass:
    def __init__(self):
        # Public variable
        self.public_variable = "I'm public!"

        # Private variable (name mangling)
        self.__private_variable = "I'm private!"

    def get_private_variable(self):
        return self.__private_variable

    def set_private_variable(self, new_value):
        self.__private_variable = new_value


# Creating an object of the class
obj = MyClass()

# Accessing public variable
print(obj.public_variable)  # Output: I'm public!

# Attempting to access private variable directly (will raise an AttributeError)
# print(obj.__private_variable)

# Accessing private variable using methods
print(obj.get_private_variable())  # Output: I'm private!

# Modifying private variable using methods
obj.set_private_variable("New private value")
print(obj.get_private_variable())  # Output: New private value
```
* In this example, public_variable is a regular public variable.
* **__private** variable is a private variable.
* Attempting to access **__private** variable directly from outside the class will result in an AttributeError.
* Instead, you can use getter and setter methods (**get_private_variable** and **set_private_variable**) to access and modify the private variable, providing a controlled way to interact with it.
* It's important to note that while name mangling adds a level of privacy, it is still possible to access private variables with some effort. The double underscores are mainly a convention, and it's essential to respect encapsulation and use the intended access methods whenever possible.


## Encapsulation
* Encapsulation is the concept of bundling data and methods that operate on the data within a single unit, i.e., a class.
* It helps in hiding the internal implementation details from the outside world.
* In this example, **__radius** is a private attribute, and access to it is controlled through getter and setter methods.
```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Private attribute

    def get_radius(self):
        return self.__radius

    def set_radius(self, new_radius):
        if new_radius > 0:
            self.__radius = new_radius
        else:
            print("Radius must be greater than 0.")
```

## Inheritance
Inheritance is a mechanism that allows a new class (subclass) to inherit properties and methods from an existing class (base class).

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Abstract method

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```
Here, Dog and Cat are subclasses of the Animal class, inheriting the name attribute and the abstract speak method.

## Polymorphism
Polymorphism allows objects of different classes to be treated as objects of a common base class. It enables the same method name to be used for different classes, promoting code reusability.

```python
def animal_sound(animal):
    return animal.speak()

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(animal_sound(dog))  # Output: "Woof!"
print(animal_sound(cat))  # Output: "Meow!"
```
Here, animal_sound function takes any object with a speak method, demonstrating polymorphism.

Conclusion
Python's support for object-oriented programming provides a powerful and flexible way to structure code. By using classes, encapsulation, inheritance, and polymorphism, developers can create modular, reusable, and maintainable software. Understanding these concepts is essential for building robust and scalable applications in Python.

* * *
| (c) TINITIATE / Venkata Bhattaram |
| :--- |