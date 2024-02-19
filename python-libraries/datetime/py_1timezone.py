""" MARKDOWN
## Python DateTime TimeZone
* Working with TimeStamps and TimeZones
* The conviennent way to work with TimeZones is to use the module `import pytz`
* Here we demonstrate, creation of date at a timezone and conversion of date to 
  various timezones, using `astimezone`
* Here is a full list of TimeZone values that can be used 
  https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
MARKDOWN"""
# MARKDOWN ```
import datetime
import pytz

################################################################################
# CREATE DATE AT A TIMEZONE
################################################################################
str_datetime = '2019-05-15 12:00:00'
l_date_time = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')

# Assign current Date to EST TimeZone
EST_TimeZone = pytz.timezone('America/New_York')
est_date = EST_TimeZone.localize(l_date_time)

print('est_date', est_date)
print('est_date timezone', est_date.tzinfo)
# est_date timezone America/New_York


################################################################################
# CONVERT A DATETIME AT A TIMEZONE TO ANOTHER TIMEZONE
################################################################################
str_datetime = '2019-12-15 12:00:00'
l_date_time = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')
print(l_date_time)
# Assign current Date to EST TimeZone
EST_TimeZone = pytz.timezone('America/New_York')
est_date = EST_TimeZone.localize(l_date_time)

print('est_date', est_date)
print('est_date timezone', est_date.tzinfo)


# Convert EST Date to GMT / UTC using "astimezone"
GMT_TimeZone = pytz.timezone('GMT')
gmt_date = est_date.astimezone(GMT_TimeZone)

print('gmt_date', gmt_date)
print('gmt_date timezone', gmt_date.tzinfo)


# Convert EST Date to INDIA TIMEZONE
IN_TimeZone = pytz.timezone('Asia/Kolkata')
india_date = est_date.astimezone(IN_TimeZone)

print('india_date', india_date)
print('india_date timezone', india_date.tzinfo)
