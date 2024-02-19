from datetime import date

# 1. Get the date
today = date.today()
print(today)

# 2. Breakdown Date data
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())

# print UNIX Epoch Time
import time

print(time.time())
# 1707520502.8757482