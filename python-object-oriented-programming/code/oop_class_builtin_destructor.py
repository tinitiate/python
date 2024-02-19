## Python Built-in Function __del__
#* Just like a Constructor, all objects that needs to be freed can be placed in 
#  the **Destructor**.
#* Usually its used to close connections, close file handler and freeing any 
#  shared data or resetting data

class DestructorDemo:

    def __init__(self):
        print('CONSTRUCTOR: Object of Class DestructorDemo Started')

    # This method, can be used to close all the connections or file handles ..    
    def __del__(self):
        print('DESTRUCTOR: Object of Class DestructorDemo Freed')

x = DestructorDemo()