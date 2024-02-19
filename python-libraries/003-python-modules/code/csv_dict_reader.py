import csv

with open('E:\\python-master\\media\\003-python-modules\\data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        # output of the reader is dictionary
        print(line)       
        
        # Getting specific column from the list in this case email.
        print(line['LastName'])