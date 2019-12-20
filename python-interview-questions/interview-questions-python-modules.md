# Python Modules Q and A

## Explain split(), sub(), subn() methods of “re” module in Python.
* To modify the strings, Python’s “re” module is providing 3 methods. They are:
split() – uses a regex pattern to “split” a given string into a list.
sub() – finds all substrings where the regex pattern matches and then replace them with a different string
subn() – it is similar to sub() and also returns the new string along with the no. of replacements.

## What is pickling and unpickling?
* Pickle module accepts any Python object and converts it into a string 
  representation and dumps it into a file by using dump function, this process is 
  called pickling. While the process of retrieving original Python objects from 
  the stored string representation is called unpickling.
