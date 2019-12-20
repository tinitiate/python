""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Modules argparse
MetaDescription: Python Modules, argparse
MetaKeywords: Python Modules, argparse
Author: Venkata Bhattaram / tinitiate.com
ContentName: python-modules-argparse
---
MARKDOWN """

""" MARKDOWN
# Python Argparse
* Python Argparse is an Python Argument Parser
* Here we demonstrate handling arguments
* Handle custom error message in case an invalid argument is passed
* Test Cases for the code below
* **ERROR Scenario:** `python F:\code\tinitiate\source\python\ti-cms-md-gen.py -s 100`
* **Single Parameter -a Scenario:** `python F:\code\tinitiate\source\python\ti-cms-md-gen.py -a 100`
* **Double Parameter -a and -b Scenario:** `python F:\code\tinitiate\source\python\ti-cms-md-gen.py -a 100 -b 2000`
MARKDOWN """

# MARKDOWN ```
import argparse
import sys

# Class to handle Custom Error Messag in case an invalid argument is passed
class MyParser(argparse.ArgumentParser):
    def error(self, message):
        # sys.stderr.write("Hello")
        print("")
        self.print_help()
        sys.exit(2)


# Function to handle the arguments and its values, to perform an action
def a(a=1, b=1, c="", **kwargs):
    if a is not None:
        print("a", a)
    elif b is not None:
        print("b", b)
    elif b is not None:
        print("c is selected")


# Function Main
if __name__ == "__main__":

    parser = MyParser()
    parser.set_defaults(method = a)
    
    # Argument
    parser.add_argument('-a', help="this is -a switch", default=1, type = int)
    parser.add_argument('-b', help="this is -b switch", default=1, type = int)
    parser.add_argument('-c', help="-c switch without parameters", action='store_true')
    args = parser.parse_args()
    args.method(**vars(args))
# MARKDOWN ```
