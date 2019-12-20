#========================================================================================
# TOPIC: PYTHON - Regular Expressions Patterns
#========================================================================================
# NOTES: * Regular Expressions are string patterns to search in other strings
#        * PYTHON Regular Expressions, functionality is provided by the "re" MODULE
#        * This program demonstrates and explains various patterns of the 
#		   regular expressions   
#        * Common Regular Expression patterns
#           Match any single character using '.'
#           Match start of line '^'
#           Match END of line '$'
#           Match any single character in brackets. [...]
#           Match any single character NOT in brackets. [^...]
#			Match Beginning of entire string '\\A'
#           Match End of entire string '\\z'
#           Match End of entire string except valid final line terminator CAPS(Z)'\\Z'
#           Match 0 or more occurrences of preceding expression. '*'
#           Match 1 or more of the preceding expression. '+'
#           Match 0 or 1 occurrence of preceding expression. '?'
#           Match exactly n number of occurrences of preceding expression. 'exp{n}'
#           Match n or more occurrences of preceding expression. 'exp{n,}'
#           Match exactly n occurrences and m times, of preceding expression.'exp{n,m}'
#           Match X OR Y. 'X|Y'
#           Match word characters '\\w'
#           Match NON word characters '\\W'
#           Match whitespace. Equivalent to [\t\n\r\f]. '\\s'
#           Match NON whitespace. NOT Equivalent to [\t\n\r\f]. '\\S'
#           Match digits. Equivalent to [0-9]. '\\d'
#           Match NON digits. '\\D'
#
#========================================================================================
#
# FILE-NAME       : 027_regular_expressions_patterns.py
# DEPENDANT-FILES : These are the files and libraries needed to run this program ;
#                   N/A
#
# AUTHOR          : tinitiate.com / Venkata Bhattaram
#                   (c) 2014
#
# DESC            : Python Regular Expressions Patterns
#
#========================================================================================

# First STEP to use Regular Expressions in python import the "re" module
import re

# Lets create a function to process the regular expression and the source string
def regEx(RegEx, TargetString, RegExPattern, ReplaceString):
"This function accepts the regex type:TargetString,the RegExPattern,the ReplaceString"
    retValue = re.sub(RegExPattern, ReplaceString, TargetString)
    print(RegEx)
    print(retValue)



RegEx = "1) Matches any single character using '.'"
TargetString = "ABCDEFG"
RegExPattern = "B(.)D"
ReplaceString = "BXD"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT:  ABXDEFG


RegEx = "2) Matches START of line '^'"
TargetString = " is a line."
RegExPattern = "^"
ReplaceString = "Here"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: Here is a line.


RegEx = "3) Matches END of line '$'"
TargetString = "This is a "
RegExPattern = "$"
ReplaceString = "line"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: This is a line


RegEx = "4) Matches any single character in brackets. [...]"
TargetString = "SAT SIT SET"
RegExPattern = "S[AI]T"
ReplaceString = "SXT"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: SXT SXT SET


RegEx = "5) Matches any single character NOT in brackets. [^...]"
TargetString = "SAT SIT SET"
RegExPattern = "S[^AI]T"
ReplaceString = "SXT"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: SAT SIT SXT


RegEx = "6) Matches Beginning of entire string '\\A' "
TargetString = "there was PASCAL"
RegExPattern = "\\A"; # Using the Escape Character "\"
ReplaceString = "Once upon a time "
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: Once upon a time there was PASCAL


RegEx = "7) Matches End of entire string '\\z' "
TargetString = "there was "
RegExPattern = "\\z" # Using the Escape Character "\"
ReplaceString = "PASCAL."
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: there was 


RegEx = "8)Matches End of entire string except valid final line terminator CAPS(Z)'\\Z'"
TargetString = "there was \n"
RegExPattern = "\\Z" # Using the Escape Character "\"
ReplaceString = "PASCAL."
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: there was 
#         PASCAL.


RegEx = "9) Matches 0 or more occurrences of preceding expression. '*'"
TargetString = "JA is Cool, JAJA is Cool"
RegExPattern = "J*"
ReplaceString = "JAVA"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: JAVAAJAVA JAVAiJAVAsJAVA JAVACJAVAoJAVAoJAVAlJAVA,JAVA 
#         JAVAAJAVAAJAVA JAVAiJAVAsJAVA JAVACJAVAoJAVAoJAVAlJAVA


RegEx = "10) Matches 1 or more of the preceding expression. '+'"
TargetString = "JA is Cool, JAJA is Cool"
RegExPattern = "J+"
ReplaceString = "JAVA"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: JAVAA is Cool, JAVAAJAVAA is Cool


RegEx = "11) Matches 0 or 1 occurrence of preceding expression. '?'"
TargetString = "JA is Cool, JAJA is Cool"
RegExPattern = "J?"
ReplaceString = "JAVA"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: JAVAAJAVA JAVAiJAVAsJAVA JAVACJAVAoJAVAoJAVAlJAVA,JAVA
#         JAVAAJAVAAJAVA JAVAiJAVAsJAVA JAVACJAVAoJAVAoJAVAlJAVA


RegEx = "12)Matches exactly n number of occurrences of preceding expression.'exp{n}'"
TargetString = "avav av avavav avavavavavav"
RegExPattern = "(av){2}"
ReplaceString = "JAVA"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: JAVA av JAVAav JAVAJAVAJAVA


RegEx = "13) Matches n or more occurrences of preceding expression. 'exp{n,}'"
TargetString = "avav av avavav avavavavavav"
RegExPattern = "(av){2,}"
ReplaceString = "JAVA"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: JAVA av JAVA JAVA


RegEx = "14)Matches exactly n occurrences and m times,of preceding expression.'exp{n,m}'"
TargetString = "avav av avavav avavavavavav"
RegExPattern = "(av){2,2}"
ReplaceString = "JAVA"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: JAVA av JAVAav JAVAJAVAJAVA


RegEx = "15) Matches X OR Y. 'X|Y'"
TargetString = "ERLANG is great"
RegExPattern = "(ERLANG|SCALA)"
ReplaceString = "JAVA"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: JAVA is great


RegEx = "16) Matches word characters '\\w'"
TargetString = "Java is great"
RegExPattern = "(\\w)"
ReplaceString = "JAVA"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: JAVAJAVAJAVAJAVA JAVAJAVA JAVAJAVAJAVAJAVAJAVA


RegEx = "17) Matches NON word characters '\\W'"
TargetString = "Java is great"
RegExPattern = "(\\W)"
ReplaceString = "JAVA"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: JavaJAVAisJAVAgreat


RegEx = "18) Matches whitespace. Equivalent to [\t\n\r\f]. '\\s'"
TargetString = "Java is        great"
RegExPattern = "(\\s)"
ReplaceString = "JAVA"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: JavaJAVAisJAVAJAVAJAVAJAVAJAVAJAVAJAVAJAVAgreat


RegEx = "19) Matches NON whitespace. NOT Equivalent to [\t\n\r\f]. '\\S'"
TargetString = "Java is        great"
RegExPattern = "(\\S)"
ReplaceString = "JAVA"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: JAVAJAVAJAVAJAVA JAVAJAVA        JAVAJAVAJAVAJAVAJAVA


RegEx = "20) Matches digits. Equivalent to [0-9]. '\\d'"
TargetString = "Java is Number 1 !!"
RegExPattern = "(\\d)"
ReplaceString = "one"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: Java is Number one !!


RegEx = "21) Matches NON digits. '\\D'"
TargetString = "1a2b3"
RegExPattern = "(\\D)"
ReplaceString = "JAVA"
regEx(RegEx, TargetString, RegExPattern, ReplaceString)
# OUTPUT: 1JAVA2JAVA3

#========================================================================================
# END OF CODE
#========================================================================================
#TAGS: Python Regular Expressions, patterns
#========================================================================================
