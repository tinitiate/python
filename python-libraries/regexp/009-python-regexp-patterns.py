""" MARKDOWN
---
Title: python regular expressions patterns
MetaKeywords: python, regular expressions patterns, code, tutorials
Author: Venkata Bhattaram / tinitiate.com
ContentName: python-regular-expressions-patterns
---
MARKDOWN """

""" MARKDOWN
# PYTHON REGULAR EXPRESSIONS PATTERNS
* Regular Expressions are string patterns to search in other strings
* PYTHON Regular Expressions, functionality is provided by the "re" MODULE
* This program demonstrates and explains various patterns of the 
  regular expressions   
* Common Regular Expression patterns
  * Match any single character using '.'
  * Match start of line '^'
  * Match END of line '$'
  * Match any single character in brackets. [...]
  * Match any single character NOT in brackets. [^...]
  * Match Beginning of entire string '\\A'
  * Match End of entire string except valid final line terminator CAPS(Z)'\\Z'
  * Match 0 or more occurrences of preceding expression. '*'
  * Match 1 or more of the preceding expression. '+'
  * Match 0 or 1 occurrence of preceding expression. '?'
  * Match exactly n number of occurrences of preceding expression. 'exp{n}'
  * Match n or more occurrences of preceding expression. 'exp{n,}'
  * Match exactly n occurrences and m times, of preceding expression.'exp{n,m}'
  * Match X OR Y. 'X|Y'
  * Match word characters '\\w'
  * Match NON word characters '\\W'
  * Match whitespace. Equivalent to [\t\n\r\f]. '\\s'
  * Match NON whitespace. NOT Equivalent to [\t\n\r\f]. '\\S'
  * Match digits. Equivalent to [0-9]. '\\d'
  * Match NON digits. '\\D'
MARKDOWN """
# MARKDOWN ```
# First STEP to use Regular Expressions in python import the "re" module
import re

# Matches any single character using '.'
# ------------------------------------------------------------------------------
TargetString = "ABCDEFG"
RegExPattern = "B(.)D"
ReplaceString = "BXD"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: ABXDEFG


# Matches START of line '^'
# ------------------------------------------------------------------------------
TargetString = " is a line."
RegExPattern = "^"
ReplaceString = "Here"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: Here is a line.


# Matches END of line '$'
# ------------------------------------------------------------------------------
TargetString = "This is a "
RegExPattern = "$"
ReplaceString = "line"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: This is a line


# Matches any single character in brackets. [...]
# ------------------------------------------------------------------------------
TargetString = "SAT SIT SET"
RegExPattern = "S[AI]T"
ReplaceString = "SXT"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: SXT SXT SET


# Matches any single character NOT in brackets. [^...]
# ------------------------------------------------------------------------------
TargetString = "SAT SIT SET"
RegExPattern = "S[^AI]T"
ReplaceString = "SXT"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: SAT SIT SXT


# Matches Beginning of entire string '\\A'
# ------------------------------------------------------------------------------
TargetString = "there was PASCAL"
RegExPattern = "\\A"; # Using the Escape Character "\"
ReplaceString = "Once upon a time "
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: Once upon a time there was PASCAL


# Matches End of entire string except valid final line terminator CAPS(Z)'\\Z'
# ------------------------------------------------------------------------------
TargetString = "there was \n"
RegExPattern = "\\Z"            # Using the Escape Character "\"
ReplaceString = "PASCAL."
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: there was 
#         PASCAL.


# Matches 0 or more occurrences of preceding expression. '*'
# ------------------------------------------------------------------------------
TargetString = "JA is Cool, JAJA is Cool"
RegExPattern = "J*"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVAAJAVA JAVAiJAVAsJAVA JAVACJAVAoJAVAoJAVAlJAVA,JAVA 
#         JAVAAJAVAAJAVA JAVAiJAVAsJAVA JAVACJAVAoJAVAoJAVAlJAVA


# Matches 1 or more of the preceding expression. '+'
# ------------------------------------------------------------------------------
TargetString = "JA is Cool, JAJA is Cool"
RegExPattern = "J+"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVAA is Cool, JAVAAJAVAA is Cool


# Matches 0 or 1 occurrence of preceding expression. '?'
# ------------------------------------------------------------------------------
TargetString = "JA is Cool, JAJA is Cool"
RegExPattern = "J?"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVAAJAVA JAVAiJAVAsJAVA JAVACJAVAoJAVAoJAVAlJAVA,JAVA
#         JAVAAJAVAAJAVA JAVAiJAVAsJAVA JAVACJAVAoJAVAoJAVAlJAVA


# Matches exactly n number of occurrences of preceding expression.'exp{n}'
# ------------------------------------------------------------------------------
TargetString = "avav av avavav avavavavavav"
RegExPattern = "(av){2}"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVA av JAVAav JAVAJAVAJAVA


# Matches n or more occurrences of preceding expression. 'exp{n,}'
# ------------------------------------------------------------------------------
TargetString = "avav av avavav avavavavavav"
RegExPattern = "(av){2,}"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVA av JAVA JAVA


# Matches exactly n occurrences and m times,of preceding expression.'exp{n,m}'
# ------------------------------------------------------------------------------
TargetString = "avav av avavav avavavavavav"
RegExPattern = "(av){2,2}"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVA av JAVAav JAVAJAVAJAVA


# Matches X OR Y. 'X|Y'
# ------------------------------------------------------------------------------
TargetString = "ERLANG is great"
RegExPattern = "(ERLANG|SCALA)"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVA is great


# Matches word characters '\\w'
# ------------------------------------------------------------------------------
TargetString = "Java is great"
RegExPattern = "(\\w)"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVAJAVAJAVAJAVA JAVAJAVA JAVAJAVAJAVAJAVAJAVA


# Matches NON word characters '\\W'
# ------------------------------------------------------------------------------
TargetString = "Java is great"
RegExPattern = "(\\W)"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JavaJAVAisJAVAgreat


# Matches whitespace. Equivalent to [\t\n\r\f]. '\\s'
# ------------------------------------------------------------------------------
TargetString = "Java is        great"
RegExPattern = "(\\s)"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JavaJAVAisJAVAJAVAJAVAJAVAJAVAJAVAJAVAJAVAgreat


# Matches NON whitespace. NOT Equivalent to [\t\n\r\f]. '\\S'
# ------------------------------------------------------------------------------
TargetString = "Java is        great"
RegExPattern = "(\\S)"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVAJAVAJAVAJAVA JAVAJAVA        JAVAJAVAJAVAJAVAJAVA


# Matches digits. Equivalent to [0-9]. '\\d'
# ------------------------------------------------------------------------------
TargetString = "Java is Number 1 !!"
RegExPattern = "(\\d)"
ReplaceString = "one"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: Java is Number one !!


# Matches NON digits. '\\D'
# ------------------------------------------------------------------------------
TargetString = "1a2b3"
RegExPattern = "(\\D)"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: 1JAVA2JAVA3

# MARKDOWN ```
