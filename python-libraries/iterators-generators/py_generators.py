"""
## PYTHON GENERATORS:
* Generators are used to create iterators, produces a sequence of 
  values into a iterator.
* Python Generators return an iterator, This is done using the 
  keyword `yield`.
* "yield" is similar to a "return" except that yield appends to a LIST 
  of values for an iterator and this iterator generated can be used
  with __next__()
MARKDOWN """

# MARKDOWN ```
################################################################################
# GENERATORS
################################################################################

#Function converted to a generator using yield
def GeneratorDemo():
    yield 22
    yield 33
    yield 44

# Call the function as an iterator
myIter = GeneratorDemo()

# print the state of the function as an iterator
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())


myIter = GeneratorDemo()
for c in myIter:
    print(c)

# Put the yield in a loop in the function to use in more scenarios
def GeneratorDemo1():
    for c1 in [1,2,3,4,5]:
        yield c1


# Call the function as an iterator
myIter = GeneratorDemo1()

# print the state of the function as an iterator
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
# print(myIter.__next__())

print("-----")
myIter = GeneratorDemo1()
print("Manual __next__() call of Iterator")
print(myIter.__next__())
print(myIter.__next__())
print("Loop Call of Iterator")
for c in myIter:
    print(c)
print("-----")

# Create Dynamic Generator
def EvenOddNum(MAX):
    num = 0
    while num < MAX:
        num += 1
        if num%2 != 0:
            yield str(num) + " is Odd Number"
        else:
            yield str(num) + " is Even Number"

# Call the function as an iterator
myIter = EvenOddNum(5)

# print the state of the function as an iterator
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
print(myIter.__next__())
# This Will Error out as MAX is 5 and this is 6TH __next__()
print(myIter.__next__())