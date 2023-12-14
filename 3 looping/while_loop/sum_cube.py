num=123
sum=0
while(num!=0):
    digit=num%10        # 123%10=3
    digit_cube=digit**3 # 3**3=27
    sum=sum+digit_cube  # 0+27
    num=num//10         # 12

print(sum)