# quantifiers
# *
# {}


from re import *
text="aaabcaabbaaaabd"
# pattern="a*"     #any no.of 'a' including zero 
# pattern="a{2}"     #contains two a
# pattern="[0-10]{2}" 
pattern="a{2,4}"   #min 2 and max 4

matcher=finditer(pattern,text)

count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
# print(count)

