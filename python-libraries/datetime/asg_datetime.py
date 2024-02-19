# Date Time Assignments

# 1. print the day name of Feb 9th for the last 10 years
import datetime

dtm = "0209"
today = datetime.datetime.today()
year = today.strftime("%Y")
year = int(year)

for c in range(11):
   dt_str = dtm+str(year)  # "0209"+str("2024") "02092024"
   print(dt_str)
   t1 = datetime.datetime.strptime(dt_str, "%m%d%Y")
   print(t1.strftime("%A"))
   year = year-1