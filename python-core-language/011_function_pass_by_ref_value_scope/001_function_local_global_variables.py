# Python Global and Local Variables
MyVar = 'This is a Global Value'

def myFunction():

    # Local Variable
    MyVar = 'This is a local variable'
    
    print('Value of MyVar inside function: ', MyVar)
# End of function code:  myFunction

# Make a call to myFunction
myFunction()
print('Value of MyVar outside function: ', MyVar) 