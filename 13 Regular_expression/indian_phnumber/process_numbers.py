from re import *
f=open("D:\\Desktop\\Python works\\Regular_expression\\numbers.txt")

rule="([+]91)?[0-9]{10}"
for line in f:
    number=line.rstrip("\n")
    matcher=fullmatch(rule,number)
    if matcher != None:
        print(number)