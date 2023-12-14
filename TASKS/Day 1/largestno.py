# 4.Write a program to find the largest number out of three numbers excepted from user.

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))

if num1>num2 and num1>num3:
    print(f"{num1} is largest")
elif num2>num1 and num2>num3:
    print(f"{num2} is largest")
else:
    print(f"{num3} is largest")