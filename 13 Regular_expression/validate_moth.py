from re import *

month=input("Enter month:")

rule="(0[1-9]|1[012])"
matcher=fullmatch(rule,month)

print("invalid" if matcher==None else "valid")