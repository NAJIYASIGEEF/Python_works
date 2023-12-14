num=int(input("Enter number: "))
is_prime=True

for i in range(2,num):
    if num%i==0:
        is_prime=False

print(is_prime)