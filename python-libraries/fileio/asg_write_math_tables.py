import os

l_file_path = "D:\\training/PythonFeb2024/"
NUM = 5

l_file_name = l_file_path+ str(NUM)+"_table.txt"

# STEP 2: Create a file in Write Mode 
new_file = open(l_file_name, "w")

for c in range(1,11):
    str_to_print = str(NUM)+" X "+str(c)+" = "+str(NUM*c)
    # 2 X 1 = 2
    # STEP 3: Write to file using write method
    # new_file.write(str_to_print+"\n")
    new_file.write(str_to_print)

new_file.close()