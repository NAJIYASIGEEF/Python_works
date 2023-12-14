# 1.Write a python program to find factorial of a prime number

fact=1
num=int(input("Enter a number:"))
is_prime=True
for i in range(2,num):
    if num%i==0:
        is_prime=False

if is_prime:
    for i in range(2,num+1):
        fact=fact*i
    print(fact)
else:
    print("Invalid")

