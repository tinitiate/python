email = "abc_rrr.123@gmail.com"
# email = "rrrt.tt.yyyy.23@yahoo.co.in"
# email = "123@microsoft.in"

# Code WRT var: email
print(email.find('@'))
at_pos = email.find('@')

cleaned_str = email[at_pos:]
print(cleaned_str)
print(cleaned_str.find('.'))

dot_pos = cleaned_str.find('.')
# print(cleaned_str[0:dot_pos])
print(cleaned_str[1:dot_pos])
