# 2.Write a python program that Take input from user and make square list of the number and the cube list .Range is 10 number in the list

square_list=[]
cube_list=[]
for i in range(1,10):
    num=int(input("Enter a number:"))
    square=num**2
    # print(f"square:{square}")
    cube=num**3
    # print(f"cube:{cube}")
    square_list.append(square)
    cube_list.append(cube)
print(f"Square list :{square_list}")
print(f"Cube list :{cube_list}")