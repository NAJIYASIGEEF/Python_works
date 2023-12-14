num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
sum=0

for i in range(num1,num2+1):
    if i%2==0:
        sum=sum+i
print(sum)
