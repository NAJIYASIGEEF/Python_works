start=1
end=int(input("Enter limit "))

i=start
while(i<=end):
    if i%2==0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
    i+=1