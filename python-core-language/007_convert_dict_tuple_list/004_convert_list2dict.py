# Converting List to Dictionary
import itertools
list1 = [1,11,2,22,3,33]
dict1 = dict(itertools.zip_longest(*[iter(list1)] * 2, fillvalue=""))
print(dict1)