import re

string = "at what time?"
match = re.findall('at',string)
print (match)

string = "at what time?"
match = re.sub("\s","!!!",string)
print (match)