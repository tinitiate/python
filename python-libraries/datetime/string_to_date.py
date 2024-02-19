""" MARKDOWN
## Python datetime strptime(): Convert String to DATE and TIME
* Use `strptime()` to convert string to date
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
* `%S`  Second as a decimal number [00,59].
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

import datetime

################################################################################
# Convert String to Date
################################################################################
l_date_time_string = "2016-06-24"
l_datetime = datetime.datetime.strptime(l_date_time_string, "%Y-%m-%d")
print(l_datetime)

# Convert String to Date Time in format; DD-MON-YYYY HH24:MI:SS
l_date_string1 = "2016-06-24 16:00:00"
format4        = "%Y-%m-%d %H:%M:%S"
t1 = datetime.datetime.strptime(l_date_string1, format4)
print("t1", t1)

# Get Todays Date Time in format4
today = datetime.datetime.today()
s = today.strftime(format4)

# Convert string s back to date time in format4
t2=datetime.datetime.strptime(s, format4).date()