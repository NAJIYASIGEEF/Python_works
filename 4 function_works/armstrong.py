def armstrong(num):
    
    sum=0
    digit_count=len(num)
    num=int(num)
    og=num
    while(num!=0):
        last_digit=num%10         
        exp=last_digit**digit_count
        sum=sum+exp
        num=num//10
    return (True if sum==og else False)   

print(armstrong("153"))