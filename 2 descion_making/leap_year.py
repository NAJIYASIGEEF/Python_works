#program to check leap year or not

year=int(input("Enter year: "))

if year%100==0 and year%400==0 or year%100!=0 and year%4==0 :
    print(f"{year} is a leap year")
else :
    print(f"{year} is not a leap year")














# only for the case of non century year not applicable for century year
# if year%4==0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not leap year")
