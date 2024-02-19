""" PYTHON Object Oriented Programming
* Python supports, Object Oriented Programming, Its a concept where data and
  functionality are combined into a unit called as CLASS.
* Class is a collection of DATA and FUNCTIONS that operate on that data
* Data could be Variables(or CLASS ATTRIBUTES) Lists, tuples, dictionaries..
* Functions are operations that perform operations on data values,
  such as get squareroot or get square of a given data set.
* For more complex business scenarios, Data could be Credit and salary
  information and the function could be approve/disapprove loan.
* Objects are instantiation of classes (reference of a class instance)
* While Class is a Spefcification, Object is the implementation 
  (or the executing instance of the class).
"""
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
