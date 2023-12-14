# 1. Write a Python program that keep on accepting number from the user until users enter zero display the sum of all number

num=int(input("Enter a number: "))
n=num
add=0

while(num!=0):
    num=int(input("Enter a number: "))
    add=add+num
sum=add+n
print(f"Sum of all numbers: {sum}")
