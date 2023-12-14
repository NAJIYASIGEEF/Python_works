from re import *
f=open("D:\\Desktop\\Python works\\Regular_expression\\vehicles\\vehicle_numbers.txt")


rule="(KL|TN)-[0-9]{2}-[A-Z]{1,2}-[0-9]{4}"
for line in f:
    number=line.rstrip("\n")
    matcher=fullmatch(rule,number)
    if matcher != None:
        print(number)

