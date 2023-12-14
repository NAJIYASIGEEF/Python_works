# 1.Write a program to accept two numbers and mathematical operators and perform operation accordingly
# Output:
# Enter 1st number :10
# Enter 2nd number:5
# Enter operator: -
# The answer:5

num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
operator=input("Enter operator:")

if operator=='+':
    add=num1+num2
    print(add)

elif operator=='-':
    sub=num1-num2
    print(sub)

elif operator=='*':
    mul=num1*num2
    print(mul)

elif operator=='/':
    div=num1/num2
    print(div)

elif operator=='%':
    mod=num1%num2
    print(mod)

elif operator=='//':
    floor=num1//num2
    print(floor)

