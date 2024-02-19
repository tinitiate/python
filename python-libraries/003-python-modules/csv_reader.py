import csv

############################################################
## Reading a csv file using csv reader method
############################################################

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)    
    # print(csv_data)    
        
    # Ignore Headers or first line of the data
    next(csv_reader)
    
    for line in csv_reader:    

        # output of the reader is list
        print(line)  

        # Getting specific column from the list in this case email.
        # print(line[2])

############################################################
## writing to csv using csv writer method
############################################################

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)    
    
    # with open('data_new.csv', 'w',newline='') as new_file:
    with open('data_new.csv', 'w') as new_file:

        # csv writer method
        csv_writer = csv.writer(new_file,delimiter='\t') 
    
        for line in csv_reader:    

            # csv method to write items in a sequence           
            csv_writer.writerow(line)
        

with open('data_new.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter='\t')  
    
    for line in csv_reader:
        print(line)
############################################################

