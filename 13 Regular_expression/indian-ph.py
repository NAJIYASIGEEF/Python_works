from re import *

phone_number=input("Enter phone number:")
rule="([+]91)?[0-9]{10}"

matcher=fullmatch(rule,phone_number)
print("invalid" if matcher==None else "valid")