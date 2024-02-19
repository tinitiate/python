tz1 = "Asia/Qyzylorda"
tz2 = "America/Caracas"
tz3 = "W-SU"

import datetime
import pytz

################################################################################
# CREATE DATE AT A TIMEZONE
################################################################################
str_datetime = '2019-05-15 12:00:00'
l_date_time = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')

# Assign current Date to tz1
tzd1 = pytz.timezone(tz1)
d1_tz = tzd1.localize(l_date_time)
print(d1_tz)
 
# Assign current Date to tz2
tzd2 = pytz.timezone(tz2)
d2_tz = tzd2.localize(l_date_time)
print(d2_tz)

# Assign current Date to tz3
tzd3 = pytz.timezone(tz3)
d3_tz = tzd3.localize(l_date_time)
print(d3_tz)
