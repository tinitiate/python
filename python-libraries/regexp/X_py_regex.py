import re

my_string = 'Hour01 Min22 VOIDDDDD Sec29 BLAH min3erere Hour32 OTHERS Min33 Hour32'


# ##############################################################################
# String Pattern Match Exact word
# From "my_string" find all words exactly like "Hour32"
# ##############################################################################

has_3 = re.findall(r'\w*3\w*', my_string)

for c in has_3:
    print(c)

