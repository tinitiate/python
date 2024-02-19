import csv

with open('D:/training/PythonFeb2024/code/python-libraries/csv/data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)    
    print(csv_reader)    
        
    # Ignore Headers or first line of the data
    # next(csv_reader)
    
    for line in csv_reader:    

        # output of the reader is list
        print(line)  

        # Getting specific column from the list in this case email.
        print(line[2])