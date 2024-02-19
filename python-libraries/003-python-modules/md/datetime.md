# Datetime 

* The `datetime` module provides classes to represent dates, times, and timestamps. Here are some key classes and methods:

  - `datetime.date`: Represents a date (year, month, day).
  - `datetime.time`: Represents a time (hour, minute, second, microsecond).

  - `datetime.datetime`: Represents a timestamp (date and time).

  - `datetime.timedelta` class can be used to perform arithmetic with dates and times. 

  - `datetime.now()`: Returns the current date and time.

  - The `strptime()` method of the `datetime` module can be used to convert a string to a `datetime` object. 

  - The `strftime()` method of the `datetime` module can be used to convert a `datetime` object to a string.

  - List of format codes available for use with the `strftime()`  and `strptime` method in Python:

    - `%Y` - year with century as a decimal number (e.g. 2023)
    - `%m` - month as a zero-padded decimal number (e.g. 01 for January, 12 for December)
    - `%B` - full month name (e.g. January, February)
    - `%b` - abbreviated month name (e.g. Jan, Feb)
    - `%d` - day of the month as a zero-padded decimal number (e.g. 01, 31)
    - `%A` - full weekday name (e.g. Monday, Tuesday)
    - `%a` - abbreviated weekday name (e.g. Mon, Tue)
    - `%H` - hour (24-hour clock) as a zero-padded decimal number (e.g. 00, 23)
    - `%I` - hour (12-hour clock) as a zero-padded decimal number (e.g. 01, 12)
    - `%p` - AM/PM designation
    - `%M` - minute as a zero-padded decimal number (e.g. 00, 59)
    - `%S` - second as a zero-padded decimal number (e.g. 00, 59)
    - `%f` - microsecond as a decimal number (e.g. 000000, 999999)
    - `%j` - day of the year as a zero-padded decimal number (e.g. 001, 365)
    - `%U` - week number of the year (Sunday as the first day of the week) as a zero-padded decimal number (e.g. 00, 53)
    - `%W` - week number of the year (Monday as the first day of the week) as a zero-padded decimal number (e.g. 00, 53)
    - `%w` - weekday as a decimal number (0 for Sunday, 6 for Saturday)
    - `%z` - UTC offset in the form +HHMM or -HHMM (empty string if the object is naive)
    - `%Z` - time zone name (empty string if the object is naive)
    - `%x` - date representation (e.g. 04/20/23)
    - `%X` - time representation (e.g. 11:34:59)
    - `%%` - a literal "%" character

    > Note that the codes are case-sensitive.
    >
    > It is important to ensure that the format string used in `strptime()` and `strftime()` matches the format of the input string and the desired output string, respectively. 

* `abs()` is a built-in Python function that returns the absolute value of a number. 

  * The function takes a single argument, which can be an integer, a floating-point number, or a complex number, and returns its absolute value. 
  * The absolute value of a number is its distance from zero on the number line, regardless of its sign.

## datetime.date

* *date* module use this module to get the current date or details of the date like month, day, year.

  ```python
  from datetime import date
  
  # Get the date
  today = date.today()
  print(today)
  
  # Breakdown Date data
  today = date.today()
  print(today.day)
  print(today.month)
  print(today.year)
  print(today.weekday())
  # MARKDOWN 
  ```

## strftime()	

* This method takes a format string that specifies the format of the output string.

  ```python
  import datetime
  
  # Convert Date to String
  today = datetime.datetime.today()
  # format YYYYMMDD
  format1 = "%Y%m%d"
  # Print Format
  s = today.strftime(format1)
  print(s)
  
  # Format DD-MON-YYYY
  format2 = "%d-%b-%Y"
  # Print Format
  s = today.strftime(format2)
  print(s)
  
  
  # Format DD-MON-YYYY HH24:MI:SS
  format3 = "%d-%b-%Y %H:%M:%S"
  # Print Format
  s = today.strftime(format3)
  print(s)
  ```

## strptime()	

* This method takes two arguments:

  * The string to be parsed
  * Format string that specifies the format of the string.

  ```python
  import datetime
  
  l_date_time_string = "2023-04-01"
  l_datetime = datetime.datetime.strptime(l_date_time_string, "%Y-%m-%d")
  print(l_datetime)
  
  # Convert String to Date Time in format; DD-MON-YYYY HH24:MI:SS
  l_date_string1 = "2023-04-01"
  format4        = "%Y-%m-%d %H:%M:%S"
  t1 = datetime.datetime.strptime(l_date_string1, format4)
  print("t1", t1)
  
  # Get Todays Date Time in format4
  s = today.strftime(format4)
  
  # Convert string s back to date time in format4
  t2=datetime.datetime.strptime(s, format4).date()
  ```

## Date Comparisons

* Below is the demonstration to compare dates.

  ```python
  import datetime
  
  # Comparision
  D1_str = "2023-04-01"
  D1 = datetime.datetime.strptime(D1_str, "%Y-%m-%d")
  print("D1 ",D1)
  
  D2_str = "2023-05-01"
  D2 = datetime.datetime.strptime(D2_str, "%Y-%m-%d")
  print("D2 ",D2)
  
  
  if(D1 > D2):
      print(D1," is Greater than ",D2)
  else:
      print(D1," is Less than ",D2)
  ```

## datetime.timedelta

* timedelta is a Python class from the datetime module that represents a duration of time, such as a number of days, hours, minutes, seconds, or microseconds.

* Using the `timedelta` we can ADD or SUBTRACT Dates amongst themselves.

* Below is the demonstration for Add Days, Hours, Minutes, Seconds to a date.

  ```python
  import datetime
  from datetime import timedelta  
  
  Date_str = '2023-04-01 12:30:22'
  formatADT = "%Y-%m-%d %H:%M:%S"
  
  D3 = datetime.datetime.strptime(Date_str, formatADT)
  print("D3 DATE-TIME",D3)
  
  # Add 5 Days to D3 using timedelta
  ######################################
  newDate = D3 + timedelta(days=5)
  s = newDate.strftime(formatADT)
  print('D3 + 5 Days', s)
  
  # Add 5 Hours to D3 using timedelta
  ######################################
  newDate = D3 + timedelta(hours=5)
  s = newDate.strftime(formatADT)
  print('D3 + 5 Hours', s)
  
  # Add 5 Minutes to D3 using timedelta
  ######################################
  newDate = D3 + timedelta(minutes=5)
  s = newDate.strftime(formatADT)
  print('D3 + 5 Minutes', s)
  
  # Add 5 Seconds to D3 using timedelta
  ######################################
  newDate = D3 + timedelta(seconds=5)
  s = newDate.strftime(formatADT)
  print('D3 + 5 Seconds', s)
  ```

* Below is the demonstration for Get difference between dates.

  ```python
  import datetime
  from datetime import timedelta  
  
  D1_str = "2023-04-01"
  D1 = datetime.datetime.strptime(D1_str, "%Y-%m-%d")
  print("D1 ",D1)
  
  D2_str = "2023-05-01"
  D2 = datetime.datetime.strptime(D2_str, "%Y-%m-%d")
  print("D2 ",D2)
  
  # Difference between TWO Dates in DAYS, Difference in Hours, Minutes and Seconds
  diff_in_days = abs(D2 - D1).days
  print(diff_in_days)
  
  # Do a Diff between Dates
  date_diff = D2 - D1
  
  # Get Diff in Hours using the total_seconds()/3600
  diff_in_hours = date_diff.total_seconds() / 3600
  print(diff_in_hours)
  
  # Get Diff in Minutes using the total_seconds()/60
  diff_in_minutes = date_diff.total_seconds() / 60
  print(diff_in_minutes)
  
  # Get Diff in Seconds using the total_seconds()
  diff_in_seconds = date_diff.total_seconds() / 60
  print(diff_in_seconds)
  ```

  









