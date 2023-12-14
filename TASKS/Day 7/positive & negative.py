# 1. Write a Python program that separate positive and negative numbers from a list


numbers=[-1,0,6,3,-4]
for i in numbers:
    if i<0:
        print(f"{i} is Negative")
    elif i>0:
        print(f" {i} is positive")
    else:
        print(f" {i} is neither positive nor negative")
