import re

'''string = 'search this inside of this text please! maha'

pattern=re.compile('search this inside of this text please!')

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
c = pattern.match(string)
print(c)

'''

#Email validation

pattern=re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)") #r- raw string
emailid = 'maha4@gmail.com'
a = pattern.search(emailid)
print(a)


#Password validation
'''
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 8 characters.
Maximum length 16 characters.
End with a number

'''
pattern=re.compile(r"[A-Za-z0-9%$#]{8,}\d") #r- raw string
passvalue = 'Supersecret%$#8l'
a = pattern.fullmatch(passvalue)
print(a)

