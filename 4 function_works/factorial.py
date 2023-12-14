def factorial (num=0):
    fact=1
    i=1
    while(i<=num):
        fact=fact*i
        i+=1
    return fact

    # for i in range(1,num+1):
    #     fact=fact*i
    # return fact

print(factorial(5))

        