# 1. The original list : [1, 3, 5, 1, 3, 2, 5, 4, 2] (user input)
# Matrix after grouping : [[1, 1], [2, 2], [3, 3], [4], [5, 5]]

number_groups = {}
original_list = [1, 3, 5, 1, 3, 2, 5, 4, 2]

for num in original_list:
    if num not in number_groups:
        number_groups[num] = [num]
    else:
        number_groups[num].append(num)

result = list(number_groups.values())
result.sort()
print(result)























# orginal_lst=[1,3,5,1,3,2,5,4,2]
# list=[]
# for row in range(1,6):
#     for col in range(1,6):
#         if row==col:
#             group=[row,col]
#             list.append(group)
# print(list)
