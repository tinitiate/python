print('Welcome to {} training of {} language'.format('tinitiate.com', 'python'));
#OUTPUT:  Welcome to tinitiate.com training of python language

print('{0} and {1}'.format('tinitiate.com', 'python'))
#OUTPUT:  tinitiate.com and python

print('{1} and {0}'.format('tinitiate.com', 'python'))
#OUTPUT: python and tinitiate.com

print('{siteName} teaches {LanguageName}.'.format(siteName='tinitiate.com', LanguageName='python'))
#OUTPUT: tinitiate.com teaches python.

#Positional and key-value arguments can be arbitrarily combined:
print('The site {0} teaches {LanguageName}'.format('tinitiate.com', LanguageName='Python'))
#OUTPUT: The site tinitiate.com teaches Python

# F String similar to ".format"
l_site = 'tinitiate.com'
l_language_name ='Python'
l_str = f"The site {l_site} teaches {LanguageName}"
pring(l_str)
