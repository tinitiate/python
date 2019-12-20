""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: python Date Time
MetaDescription: python Time Module,time.ctime(),time.time(),time.sleep(), time.strftime() Module, code, tutorials
MetaKeywords: python Date, DateTime, code, tutorials
Author: Venkata Bhattaram / tinitiate.com
ContentName: python-time
---
MARKDOWN """


""" MARKDOWN
# Python Time
* To work with date and time in python, import either time or datetime module.
* The `time` module is used for working with unix epoch time
* The `datetime` module is used for working with general date and time, 
  TimeZones and Timestamps
  
## Python time Module
* The time module works as unix epoch time, The Unix epoch start time is 
  `00:00:00 UTC on 1 January 1970`
* It is the number of seconds elapsed from the Unix epoch start time.
MARKDOWN """
# MARKDOWN ```
import time

# This gets the number of seconds elapsed from the Unix epoch start time
# 00:00:00 UTC on 1 January 1970, This is a Floating Point Number
epoch_secs = time.time()
print(epoch_secs)


# Convert Epoch secs to loca time
curr_local_time = time.ctime()
print(curr_local_time)
# MARKDOWN ```


""" MARKDOWN
## Python time Module convert time to string
* Here we demonstrate extracting parts of the date and time
* Convert date and time to string
* The following is the character to use with `strftime` to convert date to string
* *date* module use this module to get the current date or details of the 
  date like month, day, year.
* `%a`  Locale’s abbreviated weekday name.
* `%A`  Locale’s full weekday name.      
* `%b`  Locale’s abbreviated month name.     
* `%B`  Locale’s full month name.
* `%c`  Locale’s appropriate date and time representation.   
* `%d`  Day of the month as a decimal number [01,31].    
* `%f`  Microsecond as a decimal number [0,999999], zero-padded on the left
* `%H`  Hour (24-hour clock) as a decimal number [00,23].    
* `%I`  Hour (12-hour clock) as a decimal number [01,12].    
* `%j`  Day of the year as a decimal number [001,366].   
* `%m`  Month as a decimal number [01,12].   
* `%M`  Minute as a decimal number [00,59].      
* `%p`  Locale’s equivalent of either AM or PM.
* `%S`  Second as a decimal number [00,61].
* `%U`  Week number of the year (Sunday as the first day of the week)
* `%w`  Weekday as a decimal number [0(Sunday),6].   
* `%W`  Week number of the year (Monday as the first day of the week)
* `%x`  Locale’s appropriate date representation.    
* `%X`  Locale’s appropriate time representation.    
* `%y`  Year without century as a decimal number [00,99].    
* `%Y`  Year with century as a decimal number.   
* `%z`  UTC offset in the form +HHMM or -HHMM.
* `%Z`  Time zone name (empty string if the object is naive).    
* `%%`  A literal '%' character.
MARKDOWN """
# MARKDOWN ```
import time

# Convert Time to String in desired format
x = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
print(x) 

# Extract Year, Month, Month Name, Day Of Week, Day Name
Year = time.strftime("%Y", time.localtime())
Month = time.strftime("%B", time.localtime())
MonthName = time.strftime("%B", time.localtime())
DayOfWeek = time.strftime("%w", time.localtime())
DayName = time.strftime("%a", time.localtime())

print(Year)
print(Month)
print(MonthName)
print(DayOfWeek)
print(DayName)
# MARKDOWN ```


""" MARKDOWN
## Python time.sleep(): Pause code execution
* `time.sleep()` is a function that can be used to pause the code execution 
  for the specified number of seconds
MARKDOWN """
# MARKDOWN ```
import time

# Here we pause the code execution for 5 Seconds
print(time.ctime(),'Before Sleep')
time.sleep(5)
print(time.ctime(),'After Sleep')
# MARKDOWN ```
