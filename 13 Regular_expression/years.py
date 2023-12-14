# 1900-2099

from re import *

year=input("year:")

rule="(19[0-9]{2}|20[0-9]{2})"
# "(19|20)[0-9]{2}"


matcher=fullmatch(rule,year)

print("invalid" if matcher==None else "valid")