# 1. Write a Python program that accepts a string and calculates the number of digits and letters.

string=input("Enter string:")
count=(len(string))
print(f"Length of the string: {count}")

digit_count=0
string_count=0
for ch in string:
    if ch.isalpha():
        string_count+=1
    elif ch.isdigit():
        digit_count+=1

print(f"Number of letters : {string_count}")
print(f"Number of digits : {digit_count}")
