# # 2.Write a python program to accept decimal number and display it’s binary number
decimal_num=int(input("Enter decimal number:")) 
original=decimal_num

binary_num="" 
if decimal_num==0:
    binary_num=0
else:
    while decimal_num > 0:
        remainder = decimal_num % 2        
        binary_num = str(remainder) + binary_num
        decimal_num = decimal_num // 2      
print(binary_num)
