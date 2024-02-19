# ljust, center, rjust
# justify methods that add white spaces by default to
# align the string, and pad the string to the length mentioned
print ('test'.ljust(10,'+'))
# OUTPUT: test++++++
print ('test'.rjust(10,'+'))
# OUTPUT: ++++++test
print ('test1'.center(10,'+'))
# OUTPUT: +++test+++

print("Name","ABC")
print("Phone","111 222 333")

print("Name".rjust(6,' '),"ABC")
print("Phone".rjust(6,' '),"111 222 333")