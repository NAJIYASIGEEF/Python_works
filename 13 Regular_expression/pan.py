from re import *

pan_id=input("Enter PAN ID :")
rule="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(rule,pan_id)

print("invalid" if matcher==None else "valid")