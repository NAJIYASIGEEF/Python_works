num=int(input("Enter three digit number "))
sum=0

while(num!=0):
    digit=num%10        #3
    sum=sum+digit       #0+3=3
    num=num//10         #12.3//10=12

print(f"sum={sum}")

