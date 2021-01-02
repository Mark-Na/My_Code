# a way of describing patterns within search strings
# (^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$) a way to show how an email is valid or not
# credit card validating, phone number, advancd find and replace, formatting text/output, syntax highlighting
# pythex good tool, regular expressions are literal
# use \ special symbols
#\d reps 0-9, double digit \d\d
#\w letter,digit or underscore
#\s whitespace character
#\D not a digit
#\S not a whitespace 
#\W not a word character
#. any character except line break
# use \s characters instead of actual spacebar

# Quantifiers:
# + one or more
# {x} exactly x times
# {x,y} x to y times
# {x,} x or more times
# * zero or more times
# ? once or none(optional)
# [aeiou] matches any instance where there is one of these characters
# double vowels {2}[aeiou] case sensitive*
# can use range of characters a-z
# [A-Z]{2,} 2 or more uppercase characters in a row
# [^x] not x 
# ^ start of string or line
# $ end of string or line
# \b word boundary ex: \b\w+\b
#| acts as or 
# (https?://[A-Z-z_-]+\.[A-Za-z]+)

#in python: import re
# import re
# pattern = re.compile(r'\d{3} \d{3}-\d{4}')
# print(type(pattern))
# res = pattern.search("call me at 310 445-9876")
# print(res)
# print(res.group())
# res = pattern.findall("call me at 310 445-9876 or 310 446-9876 ")
# print(res)
# print(re.search(r'\d{3} \d{3}-\d{4}',"call me at 310 445-9876"))
#?P<x> can be used as a label : print(group(x))

#compilation flags
#can add in comments in the compile statement if using """ """ and re.verbose or re.X
# ignore case then you put it in the ompile function
# use multiple cases if you use bitwise or |
# sub
# first compile, then you sub

# text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"
# pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+',re.I)
# print(pattern.search(text).group())
# result = pattern.sub(r"\g<1>REDACTED",text)
# result = pattern.sub(r"\g<1> \g<2>",text)
# print(result)
#\g<1>

#swapping file names
import re
titles = ["Significant Others (1987)","Tales of the city (1978)"]
titles.sort()
print(titles)
pattern = re.compile(r'(^[\w ]+) \((\d{4})\)')
for book in titles:
    result = pattern.sub(r"\g<2> - \g<1>",book)
    print(result)