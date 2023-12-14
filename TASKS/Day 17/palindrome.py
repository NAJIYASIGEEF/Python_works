# 2. Python program to check if the given string is a palindrome.

string_val=input("Enter the String: ")
str=""
for word in string_val:
    str=word+str
if string_val==str:
    print("palindrome")
else:
    print("not palindrome")
    
    