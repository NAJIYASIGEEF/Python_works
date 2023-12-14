from re import *

f=open("D:\\Desktop\\Python works\\Regular_expression\\places\\train.txt")

rule="[0-9]{5}"

for line in f:
    words=line.rstrip("\n")
    matcher=finditer(rule,words)
    for m in matcher:
        print(m.group())



# for line in f:
#     lst=line.rstrip("\n").split(" ")
#     for num in lst:
#         matcher=fullmatch(rule,num)
#         if matcher!= None:
#             print(num)