# lst=[2,3,4,5,6,7,8,9,10]
# squares=[]

# for  num in lst:
#     sq=num**2
#     squares.append(sq)

# print(f"list of squares {squares}")

# even=[]
# for num in lst:
#     if num%2==0:
#         even.append(num)
# print(f"list of even numbers: {even}")



# [return value for loop  condition] ---- list comprehension


lst=[2,3,4,5,6,7,8,9,10]
cubes=[num**3 for num in lst ]
print(cubes)


square=[num**2 for num in lst]
print(square)

even=[num for num in lst if num%2==0]
print(even)


odd=[num for num in lst if num%2!=0]
print(odd)

num_gt_5=[num for num in lst if num>5]
print(num_gt_5)


c4=["manoj","bilal","akash","malavika","jamiya"]

upper_case=[name.upper() for name in c4]
print(upper_case)

name_gt_5letters=[name for name in c4 if len(name)>5]
print(name_gt_5letters)



# lst=["red","green",blue,white,apple,ignore under]
# q1 print words starting with vowels
# starting with consosnants