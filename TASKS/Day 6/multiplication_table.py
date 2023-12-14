# 2.Write a python program to display multiplication table of a number (user input)

number=int(input("Enter a number: "))
for i in range(1,11):
    res=number*i
    
    print(f"{number}x{i}={res}")


