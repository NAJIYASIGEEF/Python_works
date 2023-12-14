# 2.Write a python program to display Fibonacci series and specify that number odd or even

num1=0
num2=1
for i in range(0,10):
    num3=num1+num2
    print(num1,end="-")
    even_odd="even" if num1%2==0 else  "odd"
    print(even_odd)
    num1=num2
    num2=num3

    