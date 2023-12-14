# PAN card

from re import *

phone_number=input("Enter american phone number:")

rule="[+][1][0-9]{3}[0-9]{3}[0-9]{4}"

matcher=fullmatch(rule,phone_number)

print("invlaid" if matcher==None else "valid")