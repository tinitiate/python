# The following loop exits before  5 iterations
for c in range(5):
    if c == 3:
        break
    print(c)

print("---")
# Nested for loop break
for c in range(5):
    for d in range(5):
        print(c,d)
        if d == 2:
            break
            # print(12)
        
"""
# Using break with while loop
cur_value = 0                  # SETUP a condition criteria
while (cur_value < 5):
    cur_value += 1  # same as curr_value = curr_value + 1
    if cur_value==3:
        break
    print('Cur_value: ', cur_value)
"""