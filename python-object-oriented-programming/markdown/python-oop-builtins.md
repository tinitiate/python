![Tinitiate Python Training](../images/python-tinitiate.png)
# Python BuiltIns
* Python's Object-Oriented Programming (OOP) is a powerful paradigm that allows developers to create objects that encapsulate both data and behavior.
* In this context, there are several built-in variables (often called "dunder" methods or attributes) that facilitate the OOP process.
* These built-in variables start and end with double underscores, like __init__, __str__, __repr__, and more.

## Constructor __init__ Method
*The __init__ method is used for initializing an object's attributes. It's called when an object is created.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of Dog
my_dog = Dog("Buddy", 5)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 5
```

## __str__ Method
* The __str__ method returns a string representation of the object. It's used for the "informal" or readable string representation.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."

my_dog = Dog("Buddy", 5)
print(my_dog)  # Output: Buddy is 5 years old.
```

## __repr__ Method
* The __repr__ method returns an "official" string representation of the object. It's typically used for debugging and logging.
```python
Copy code
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"

my_dog = Dog("Buddy", 5)
print(repr(my_dog))  # Output: Dog('Buddy', 5)
```

## __dict__ Attribute
* The __dict__ attribute is a dictionary containing an object's attributes.
```python
Copy code
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Buddy", 5)
print(my_dog.__dict__)  # Output: {'name': 'Buddy', 'age': 5}
```

## __class__ Attribute
* The __class__ attribute references the class to which an instance belongs.
```python
class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Buddy")
print(my_dog.__class__)  # Output: <class '__main__.Dog'>
```

## __doc__ Attribute
* The __doc__ attribute retrieves the documentation string of a class or a function.
```python
class Dog:
    """This class represents a dog."""
    def __init__(self, name):
        self.name = name

print(Dog.__doc__)  # Output: This class represents a dog.
```

* * *
| (c) TINITIATE / Venkata Bhattaram |
| :--- |