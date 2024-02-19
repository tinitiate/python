import csv
with open('E:\\python-master\\media\\003-python-modules\\data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)    
    
    # with open('data_new.csv', 'w',newline='') as new_file:
    with open('E:\\python-master\\media\\003-python-modules\\data_new.csv', 'w') as new_file:

        # csv writer method
        csv_writer = csv.writer(new_file,delimiter='\t') 
    
        for line in csv_reader:    

            # csv method to write items in a sequence           
            csv_writer.writerow(line)