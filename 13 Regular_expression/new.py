# starting with k,l,m or n
# second place must be a digit and divisible by 3
# followed by any number of digits and numbers
from re import *

variable_name=input("Enter variable name: ")
rule="[k-nK-N][369][a-zA-Z0-9]*"

matcher=fullmatch(rule,variable_name)

print("invalid" if matcher==None else "valid")