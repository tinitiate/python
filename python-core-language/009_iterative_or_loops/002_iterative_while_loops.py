
"""
# The below syntax loops until curr_value reaches 5
# looping 5 times using while loop 
curr_value = 0                  # SETUP a condition criteria
while (curr_value < 5):
    curr_value += 1  # same as curr_value = curr_value + 1
    print('Curr_value: ', curr_value)

"""
curr_value = 0                  # SETUP a condition criteria
while (curr_value < 5):
    print('Curr_value: ', curr_value)
    curr_value += 1  # same as curr_value = curr_value + 1

print("-----")
curr_value = 0                  # SETUP a condition criteria
while (curr_value <= 5):
    print('Curr_value: ', curr_value)
    curr_value += 1  # same as curr_value = curr_value + 1

"""
# INFINITE LOOP issue
# great care should be taken when writing loops as it could iterate perpetually or
# run in an infinite loop,while some situations require to run forever like services

# CODE
#  while(1==1)
#      print("in infinite loop")
"""