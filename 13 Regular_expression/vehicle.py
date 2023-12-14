from re import *

vehicle_no=input("Enter vehicle number:")

rule="(KL)-?[0-9]{2}-?[A-Z]{1,2}-?[0-9]{4}"

matcher=fullmatch(rule,vehicle_no)
print("invalid" if matcher==None else "valid")