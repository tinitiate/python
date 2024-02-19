data = ""
terminate_str = ":END"  # Termination String ':END'

print("Enter multiline user input, Please enter the string ':END'")
print("to terminate reading input")
while True:
    l_UserInput = input()
    if l_UserInput.strip() == terminate_str:
        break
    data = data + "\n" + l_UserInput

print(data)
