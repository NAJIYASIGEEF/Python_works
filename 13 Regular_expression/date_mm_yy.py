from re import *

date=input("Enter date:")
rule="(0?[1-9]|[12][0-9]|3[01])-(0?[1-9]|1[012])-(16|17|18|19|20)[0-9]{2}"

matcher=fullmatch(rule,date)
print("invalid" if matcher==None else "valid")