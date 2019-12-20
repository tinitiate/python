## >---
## >YamlDesc: CONTENT-ARTICLE
## >Title: Python User Input
## >MetaDescription: python user input, reading from keyboard example code, tutorials
## >MetaKeywords: python user input, reading from keyboard example code, tutorials
## >Author: Venkata Bhattaram / tinitiate.com
## >ContentName: user-input
## >---

## >#  Python User Input
## >* Python provides various methods to read user input.
## >* Reading single line user input using input (raw_input)
## >* Reading multi line user input using input (raw_input)
## >* Reading python file command line arguments


## > ## Reading Single Line Input
## >* Input text is captured until an **Enter** or **NewLine** character is 
## >  encountered.
## >```
# This is required to read python file command line arguments
import sys;

# Reading single line user input using "input"
l_UserInput = input("Enter text and press enter: ")
print ("text entered " + l_UserInput)
## >```


## >## Reading Single Line Input
## >* Reading multi line user input using input (raw_input)
## >* Multiline input is captured untill a **termination** string is 
## >  encountered, **termination** can be defined to be any text string.
## >* The **termination** String is case sensitive.
## >```
l_UserInput = ""
terminate_str = ":END"  # Termination String ':END'

print("Enter multiline user input, Please enter the string ':END'")
print("to terminate reading input")
while True:
    data = input()
    if data.strip() == terminate_str:
        break
    l_UserInput += "%s\n" % data

print(l_UserInput)
## >```


## >## Reading Python Script Command Line Arguments
## >* When executing a Python script at the Commandline arguments, we use `python file_name.py`
## >* Values can be passed to the python script, and these values are called as 
## >  arguments, They are passed as below example:
## >*  `python file-name.py argument1 argument2 ...`
## >* Python script arguments can be read using the `sys.argv`
## >```
# The sys.argv returns all the arguments to this list.
commandline_args_list = sys.argv

print(commandline_args_list)

# Call the program using
# $ python 016_reading_keyboard_input.py argument1 argument2
# The FIRST element in the list is the file path and name
## >```
