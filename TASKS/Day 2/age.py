# 2. Take input of age of 3 people by user and determine oldest and youngest among them.

age1=int(input("Enter age1:"))
age2=int(input("Enter age2:"))
age3=int(input("Enter age3:"))

if age1>age2 and age1>age3:
    print(f"{age1} is the oldest")
elif age1<age2<age3:
    print(f"{age1} is the youngest")


if age2>age3 and age2>age1:
    print(f"{age2} is the oldest")
elif age2<age1<age3:
    print(f"{age2} is the youngest")


if age3>age1 and age3>age1:
    print(f"{age3} is the oldest")
elif age3<age1<age2:
    print(f"{age1} is the youngest")

