# Python Internals Q and A

## Differences between 2.7 Vs 3.x ?
* Python 2.7
  * Legacy Version
  * Newer Libraries are not compatible
  * Strings are stored as ASCII (Uses Fixed 7 BITS to store strings)
  * print is a keyword
  * For 3.X compatibility __future__ module is used
  * Integer Division results in Integer (only character ignoring the mantissa)
* Python 3.X
  * Latest Version
  * Some Old Libraries are not compatible
  * Strings are stored as Unicode (Uses Variable 8-16-32 BITS to store strings)
  * print is a function
  * Integer Division results in double as applicable

## How Python is interpreted?
* Python language is an interpreted language, It directly runs from source code.
* Source code is converted to byte code and executed on the Python Virtial machine.
* Whenever Python has write access in the source code directory, it will 
  create a compiled byte code (.pyc) file, this is stored in the `__pycache__`
  folder it creates.
* The compiled byte code (.pyc) file, will be executed and if exists the code 
  will execute faster.
* When Python has no write access to the source code directory, The byte code 
  will be in memory and discarded after code execution.

## How memory is managed in Python?
* Python Memory
  * Heap memory
   * Heap for dynamic memory allocation.
   * Objects and instance variables values are created in Heap memory.
  * Stack memory
    * Stack is used for static memory allocation.
    * Once values are assinged values stack memory is kicked in,
      Methods and variables are created in Stack memory.
    * A stack frame is created for handling methods and variables during execution
      and stacks frames are destroyed automaticaly whenever functions/methods returns.
* Garbage collector, Once the Objects and functions returns, Garbage collector 
  clears the objects.
