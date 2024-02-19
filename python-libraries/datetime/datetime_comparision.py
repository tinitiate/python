""" MARKDOWN
## Python time Module: Date Comparisions and Checking
* Below is the demonstration to compare dates
MARKDOWN"""
# MARKDOWN ```

import datetime

# Comparision
D1_str = "2016-06-24"
D1 = datetime.datetime.strptime(D1_str, "%Y-%m-%d")
print("D1 ",D1)

D2_str = "2016-07-24"
D2 = datetime.datetime.strptime(D2_str, "%Y-%m-%d")
print("D2 ",D2)


if(D1 > D2):
    print(D1," is Greater than ",D2)
else:
    print(D1," is Less than ",D2)