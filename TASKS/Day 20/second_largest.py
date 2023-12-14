# 1. Write a Python program to find the second largest number in a list.
# Python program to find the second largest number in a list.
lst = [41, 22, 13, 14, 55]

largest=0

for num in lst:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == num:
    print("There is no second largest number.")
else:
    print("Second largest number:", second_largest)
