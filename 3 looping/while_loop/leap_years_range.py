starting_year=int(input("Enter starting year"))
current_year=2023

i=starting_year
while(i<=current_year):
    year=i
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        print(year)
    i+=1

