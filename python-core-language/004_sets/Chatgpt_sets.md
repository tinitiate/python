Sets in Python

In Python, a set is an unordered collection of unique elements. Sets are used to store a collection of distinct values without any specific order. They are particularly useful for tasks that involve membership testing, elimination of duplicates, and set operations.

Creating Sets
You can create a set in Python by enclosing a comma-separated sequence of elements within curly braces {}:

python
Copy code
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}
mixed_set = {42, "hello", 3.14, True}
Set Operations
Sets support various set operations, such as union, intersection, difference, and more:

union(): Returns a set containing all the distinct elements from both sets.
intersection(): Returns a set containing the common elements between two sets.
difference(): Returns a set containing the elements present in the first set but not in the second set.
symmetric_difference(): Returns a set containing the elements that are in either of the sets, but not in their intersection.
python
Copy code
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)                  # {1, 2, 3, 4, 5, 6}
intersection_set = set1.intersection(set2)    # {3, 4}
difference_set = set1.difference(set2)        # {1, 2}
symmetric_difference_set = set1.symmetric_difference(set2)  # {1, 2, 5, 6}
Modifying Sets
Sets are mutable, meaning you can modify their contents after creation. You can add or remove elements using methods like add() and remove():

python
Copy code
fruits = {"apple", "banana", "orange"}
fruits.add("grape")         # {"apple", "banana", "orange", "grape"}
fruits.remove("banana")     # {"apple", "orange", "grape"}
Set Membership
You can check for membership in a set using the in keyword:

python
Copy code
fruits = {"apple", "banana", "orange"}
is_apple_present = "apple" in fruits      # True
is_mango_present = "mango" in fruits      # False
Set Comprehensions
Similar to list comprehensions, you can use set comprehensions to create sets based on existing sets:

python
Copy code
numbers = {1, 2, 3, 4, 5}
squared_numbers = {x ** 2 for x in numbers}  # {1, 4, 9, 16, 25}
Immutable Sets
Python also has an immutable version of sets called frozensets. Frozensets cannot be modified after creation and can be used as elements of other sets or dictionaries.

python
Copy code
immutable_set = frozenset([1, 2, 3])
Conclusion

Sets are versatile data structures in Python that allow you to store unique elements and perform various set operations. They are useful for tasks involving distinct values, membership testing, and performing set-based calculations. Understanding sets can greatly enhance your ability to work with unique collections of data in Python.