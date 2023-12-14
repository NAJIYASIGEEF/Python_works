def add(n1,n2):
    res=n1+n2
    return res
print(add(10,20))


def smart_sub(n1,n2):
    res=n1-n2 if n1>n2 else n2-n1
    return res
print(smart_sub(10,20))


def mul(n1,n2):
    mul=n1*n2
    return mul
print(mul(10,20))


def div(n1,n2):
    div=n1/n2
    return div
print(div(10,20))