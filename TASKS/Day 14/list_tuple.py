# 1. Write a python program to create a list of tuples having first element as the number and second element as the cube of the number

num=int(input("Enter a number: "))
number_list=[]
cube_list=[]
for i in range(1,num+1):
    cube=i**3
    # num+=1
    number_list.append(i)
    cube_list.append(cube)
for i in range(0,num):

    print((number_list[i],cube_list[i]))