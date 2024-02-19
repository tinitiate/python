""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: python lambda Map Filter Reduce
MetaDescription: python lambda, Map, Filter, Reduce, code, tutorials
MetaKeywords: python lambda, Map, Filter, Reduce, code, tutorials
Author: Venkata Bhattaram / tinitiate.com
ContentName: python-lambda
---
MARKDOWN """

""" MARKDOWN
# Python Lambda Expressions
* Lambdas Expressions or Lambdas are one liner syntax to create 
  anonymous functions called Lambdas, They allow functionality and 
  data to be passed around in a single line.
* They provide a shortcut to expressions, LOOP and IF..ELSE conditions.
MARKDOWN """

""" MARKDOWN
## Python Lambda Demonstration
* Below example demonstrates Normal Function and its `lambda` equvalent
MARKDOWN """

# MARKDOWN ```
# NORMAL FUNCTION
# Function to Add 2 Numbers
def Add2Nums(Num1, Num2):
    return Num1+Num2;

# LAMBDA FUNCTION
# Function to Add 2 Numbers
AddLda = lambda x,y: x+y
print(AddLda(1,3))
# MARKDOWN ```


""" MARKDOWN
* Below example demonstrates `lambda` with IF..ELSE condition
MARKDOWN """

# MARKDOWN ```
# NORMAL FUNCTION With IF..ELSE
# Function Identify if EVEN or ODD
def EvenOrOdd(Num1):
    if(Num1%2 == 0):
        return "EVEN";
    else:
        return "ODD";

# LAMBDA FUNCTION
# Lambda Identify if EVEN or ODD
EvenOrOddLda = lambda x: 'EVEN' if(x%2==0) else 'ODD'

print(EvenOrOddLda(12))
# MARKDOWN ```


""" MARKDOWN
## Python Map Function with Lambda
* Map function applies or MAPS a single or multiple Functions sequentialy
  to each element in a source iteration from (list, dictionary, tuples)
* It executes the function_object for each element in the source iteration
  and returns a list of the elements modified by the source function(s)
* USAGE: map(someFunction, someSequence)
MARKDOWN """

# MARKDOWN ```
# MAP Single Function with an Iteration with Lambda
sequence = [2, 3, 4, 5, 6]
y = list(map(lambda v : v * 5, sequence))

print(y)

# MAP Multiple Functions with an Iteration with Lambda
def Add2(x):
        return (x+2)

def Add3(x):
        return (x+3)

MyFunctions = [Add2, Add3]

for num in range(5):
    data = list(map(lambda x: x(num), MyFunctions))
    print(data)
# MARKDOWN ```


""" MARKDOWN
## Python Filter Function Lambda Expressions
* Filter function works with two arguments a Function and Source iterable.
* The function is called for each element of the iterable with filter
  returning only elements which qualify for a given condition.
* Unlike map function filter function can only have one iterable as input.
MARKDOWN """

# MARKDOWN ```
# FILTER Function
# Removes list of a values that dont match the criteria
# Create a List of Even Numbers Only
evenList = list( filter((lambda x: x%2 == 0), range(10)))
print(evenList)

# Create a List of Salary only > 1000
salary_list = [100, 2000, 300, 4000]

list_1000_PLUS = list( filter((lambda x: x>1000), salary_list))
print(list_1000_PLUS)
# MARKDOWN ```


""" MARKDOWN
## Python Reduce Function with Lambda Expressions
* REDUCE Function
* Import Reduce from functools in Python 3X
* Accepts a function and list of values to return a single value
* by processing the result over and over untill a single value remains
MARKDOWN """

# MARKDOWN ```
from functools import reduce

addData = reduce((lambda x,y:x+y),range(10))
print(addData)

mulData = reduce((lambda x,y:x*y),range(1,10))
print(mulData)
# MARKDOWN ```
