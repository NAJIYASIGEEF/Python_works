def oneth_smallest(n1,n2):
    n=n1%10
    m=n2%10
    if n<m:
        return n1
    else:
        return n2
    
print(oneth_smallest(432,18))