# def add_numbers(n1,n2):
#     return n1+n2
# def add_numbers(n1,n2,n3):
#     return n1+n2+n3


#####################################
# def add_numbers(*args):
#     return sum(args)

# print(add_numbers(10,20))
# print(add_numbers(10,20,30))


#####################################
# def last_digit_sum(*args):
#     last_digit=[n%10 for n in args]
#     return sum(last_digit)
# print(last_digit_sum(19,23,45))


######################################
# def max_last_digit(*args):
#     l_digit=[n%10 for n in args]
#     return max(l_digit)
# print(max_last_digit(20,45,33,57))


#######################################
# def add_employee(*args):
#     print(args)

# add_employee(10,"Hari","TVM",24000)

#######################################
# def add_employe(*args):
    # print(args)

# add_employe(id=10,name="Hari",place="TVM",salary=24000)

######################################
# def my_fun(*args,**kwrgs):
    # print(args)
    # print(kwrgs)
# my_fun(1,2,3,4,reverse=True)

########################################

def last_digit_sort(*args,**kargs):

    digits=[ n%10 for n in args]
    value=kargs.get("reversed")
    if value==True:
        digits.sort(reverse=True)
    else:
        digits.sort()
    return digits

print(last_digit_sort(17,12,14,3,1,reversed=True))

                    