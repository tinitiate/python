import csv

############################################################
## Reading a csv file using csv dict reader method
############################################################

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        # output of the reader is dictionary
        print(line)       
        
        # Getting specific column from the list in this case email.
        # print(line['LastName'])

############################################################
## writing to csv using csv dict writer method
############################################################

with open('data.csv', 'r') as csv_file:    
    csv_reader = csv.DictReader(csv_file)    
    
    with open('data_new.csv', 'w') as new_file:        
        fieldnames =['FirstName','LastName','Email','Amount','MaxAmount','Status','Country','Start']

        # csv dict writer method       
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t') 

        # csv method to write the header
        csv_writer.writeheader()
    
        for line in csv_reader:  

            # csv method to write items in a sequence            
            csv_writer.writerow(line)


########################################################################
## writing to csv only specific columns using csv dict writer method
########################################################################

with open('data.csv', 'r') as csv_file:    
    csv_reader = csv.DictReader(csv_file)    
    
    with open('data_new.csv', 'w') as new_file:        
        fieldnames =['FirstName','LastName','Email','Amount','Status','Country','Start']
        
        # fieldnames=fieldnames,
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t') 
    
        for line in csv_reader:    
            del line['MaxAmount']          
            csv_writer.writerow(line)
