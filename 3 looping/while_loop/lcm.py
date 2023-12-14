
# find gcd of two numbers

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))

sm_num=num1 if num1<num2 else num2
gcd=1
i=1

while(i<=sm_num):
    if(num1%i==0 and num2%i==0):
        gcd=i
    i+=1

print(f"gcd= {gcd}")

val=num1*num2
lcm=val//gcd

print(f"lcm= {lcm}")