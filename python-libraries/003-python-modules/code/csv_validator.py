import csv
import re
import sys
import logging
from datetime import datetime
from csvvalidator import *

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('validation.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# specify the field names for the CSV
field_names = ('id', 'first_name', 'last_name', 'gender', 'age', 'date', 'is_student', 'timestamp', 'email', 'score')

# create a new CSVValidator object with the specified field names
validator = CSVValidator(field_names)

# add header check to the validator
validator.add_header_check('EX1', 'Invalid header')

# add record length check to the validator
validator.add_record_length_check('EX2', 'Invalid record length')

# add validation rules for each field to the validator
validator.add_value_check('id', lambda value: re.match(r'^\d{2}-\d{7}$', value) is not None, 'ID must be in the format XX-XXXXXXX')
validator.add_value_check('first_name', lambda value: len(value) > 0 and len(value) <= 50, 'First name cannot be empty or more than 50 characters')
validator.add_value_check('last_name', lambda value: len(value) > 0 and len(value) <= 50, 'Last name cannot be empty or more than 50 characters')
validator.add_value_check('gender', lambda value: value in ['Male', 'Female'], 'Gender must be either Male or Female')
validator.add_value_check('age', number_range_inclusive(0, 120, int), 'EX7', 'Age must be a positive integer')
validator.add_value_check('date', datetime_string('%d/%m/%Y'), 'EX8', 'Date must be in the format dd/mm/yyyy')
validator.add_value_check('is_student', lambda value: value.lower() in ['true', 'false'], 'is_student must be True or False')
validator.add_value_check('timestamp', lambda value: datetime.strptime(value, '%Y-%m-%d %H:%M:%S'), 'Timestamp must be in the format YYYY-MM-DD HH:MM:SS')
validator.add_value_check('email', lambda value: re.match(r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$', value), 'Email must be a valid email address')
validator.add_value_check('score', lambda value: isinstance(float(value), float), 'Score must be a floating point number')

# validate the data and write problems to a log file
data = csv.reader(open('E:/python-master/media/003-python-modules/sample-data.csv', 'r'), delimiter=',')
exceptions_msg = validator.validate(data)

if len(exceptions_msg) == 0:
    print('CSV is valid')
    logger.info('CSV is valid')
else:
    logger.warning(f'CSV is invalid. Found {len(exceptions_msg)} exceptions.')
    for exception in exceptions_msg:
        logger.warning(exception)
