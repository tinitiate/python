""" MARKDOWN
## Python datetime strftime(): Convert DATE and TIME to String
* Use `strftime()` to convert date to string
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

s = today.strftime("%A")
print(s)
