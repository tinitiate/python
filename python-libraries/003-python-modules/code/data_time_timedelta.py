import datetime
from datetime import timedelta  

################################################################################
# Subtracting Dates
################################################################################
D1_str = "2016-06-24"
D1 = datetime.datetime.strptime(D1_str, "%Y-%m-%d")
print("D1 ",D1)

D2_str = "2016-07-21"
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

################################################################################
# Adding to Date - Times
################################################################################
D3_str = '2016-07-21 12:30:22'
formatADT = "%Y-%m-%d %H:%M:%S"

D3 = datetime.datetime.strptime(D3_str, formatADT)
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
