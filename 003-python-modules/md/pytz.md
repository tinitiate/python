# Pytz

* The `pytz` module provides support for working with timezones in Python.

* The `pytz` module includes a database of timezone information that is based on the IANA Time Zone Database.

* We can use the `all_timezones` attribute to get a list of all the available timezone names.

* We can use the `country_timezones()` function to get a list of timezone names for a specified country code.

* The `datetime.astimezone()` method can be used to convert an aware datetime object to a different timezone.

* `pytz.timezone()`: Returns a timezone object for a specified timezone.

* `localize()`: Associates a timezone with a naive datetime object to create an aware datetime object.

* `normalize()`: Adjusts a datetime object to a specified timezone by handling daylight saving time transitions.

* `utc`: A timezone object for Coordinated Universal Time (UTC).

* `tzinfo`: A base class for implementing timezone information for datetime objects.

* We demonstrate, creation of date at a timezone and associates a timezone with datetime object using `localize`

  ```python
  import datetime
  import pytz
  
  str_datetime = '2023-04-19 12:00:00'
  l_date_time = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')
  
  # Assign current Date to EST TimeZone
  EST_TimeZone = pytz.timezone('America/New_York')
  est_date = EST_TimeZone.localize(l_date_time)
  
  print('est_date', est_date)
  print('est_date timezone', est_date.tzinfo)
  ```

* We demonstrate, creation of date at a timezone and conversion of date to various timezones, using `astimezone`

  ```python
  import datetime
  import pytz
  
  str_datetime = '2019-05-15 12:00:00'
  l_date_time = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')
  
  # Assign current Date to EST TimeZone
  EST_TimeZone = pytz.timezone('America/New_York')
  est_date = EST_TimeZone.localize(l_date_time)
  
  print('est_date', est_date)
  print('est_date timezone', est_date.tzinfo)
  ```

  

* >Here is a full list of TimeZone values that can be used 
  >
  >https://en.wikipedia.org/wiki/List_of_tz_database_time_zones