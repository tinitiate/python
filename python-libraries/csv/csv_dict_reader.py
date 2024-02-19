import csv

with open('D:/training/PythonFeb2024/code/python-libraries/csv/data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        # output of the reader is dictionary
        print(line)       
        
        # Getting specific column from the list in this case email.
        print(line['LastName'])