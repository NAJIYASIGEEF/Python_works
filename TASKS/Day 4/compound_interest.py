# 2. Write a python program to find compound interest
principal=int(input("Enter principal amount:"))
rate=float(input ("Enter rate: "))
year=int(input("Enter years:"))
n=int(input("Enter no.of times interest applied:"))

amount=principal*(1+rate/n)**(n*year)
c_interest=amount-principal

print(c_interest)