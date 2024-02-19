import csv
with open('E:\\python-master\\media\\003-python-modules\\data.csv', 'r') as csv_file:    
    csv_reader = csv.DictReader(csv_file)    
    
    with open('E:\\python-master\\media\\003-python-modules\\data_new.csv', 'w') as new_file:        
        fieldnames =['FirstName','LastName','Email','Amount','MaxAmount','Status','Country','Start']

        # csv dict writer method       
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t') 

        # csv method to write the header
        csv_writer.writeheader()
    
        for line in csv_reader:  

            # csv method to write items in a sequence            
            csv_writer.writerow(line)

####################################################################
## Writing to csv only specific columns using `csv.DictWriter`
####################################################################

import csv
with open('E:\\python-master\\media\\003-python-modules\\data.csv', 'r') as csv_file:    
    csv_reader = csv.DictReader(csv_file)    
    
    with open('E:\\python-master\\media\\003-python-modules\\data_new2.csv', 'w') as new_file:        
        fieldnames =['FirstName','LastName','Email','Amount','Status','Country','Start']
        
        # fieldnames=fieldnames,
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t') 
    
        for line in csv_reader:    
            del line['MaxAmount']          
            csv_writer.writerow(line)