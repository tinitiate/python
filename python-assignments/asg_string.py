"""
#  Find the Domain name from Email
# ####################################
email = "aaa.ddd.rrr_12@gmail.com"
# email = "a.rrr.12@yahoo.co.in"
# email = "aa_ddd_12@microsoft.com"

print(email)

v_at_pos = email.find('@')

v_cleaned_str = email[v_at_pos:]
print(v_cleaned_str)

v_dot_pos = v_cleaned_str.find(".")
print(v_dot_pos)

print(v_cleaned_str[1:v_dot_pos])
"""

# Swap Values between 2 variables
# ####################################

a = 100
b = 200

print("before a",a)
print("before b",b)

# Option 1, use a 3rd variable
c = a
a = b
b = c
print("after a",a)
print("after b",b)

# Option 2, without intermediate variable

a = 100
b = -200
print("before a",a)
print("before b",b)

b = b+a
a = b-a
b = b-a
print("after a",a)
print("after b",b)


# Scenario 2 (strings), without intermediate variable

a = "LEARN"
b = "PYTHON"
print("before a",a)
print("before b",b)

b = a+b          # LEARNPYTHON
a = b.lstrip(a)  # PYTHON
print(a)
print(b)
# b = b.rstrip(a)  # LEARNPYTHON
b = b.strip(a)  # LEARNPYTHON

print("after a",a)
print("after b",b)

# https://stackoverflow.com/questions/1687171/why-does-str-lstrip-strip-an-extra-character