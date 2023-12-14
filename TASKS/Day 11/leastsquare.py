# 2.Write a python program to find the least square number from a list\

list1=[25,16,11,23,45,4]
sqrt_lst=[]
for num in list1:
    sqrt=int(num**0.5)
    sqrt_lst.append(sqrt**2)
# sort_lst=sorted(list1)
squareroots=[n for n in list1 if n in sqrt_lst]
least_sqrt=min(squareroots)
print(f"List:{list1}")
print(f"Least squareroot from the list : {least_sqrt}")










# x=[1,2,3,4,5]
# y=[1,2,4,5,6]

# mean1 = sum(x) / len(x)
# # print(mean1) //3
# least_square_x = min(x, key=lambda x: (x - mean1) ** 2) 

# mean2 = sum(y) / len(y)
# least_square_y = min(x, key=lambda y: (y - mean2) ** 2)


# print(f"Least square number in x: {least_square_x}")
# print(f"Least square number in y: {least_square_y}")