# 1. Write a python program to identify unique triplets whose three elements sum to zero from an array of n integers
numbers=[1,-1,2,3,1,0,4]
triplet_list=[]
c=0
triplet_set=set()
for i in numbers:
    for j in numbers:
        t=-(i+j)
        if t in numbers:
            temp_list=[i,j,t]
            temp_list.sort()
            while temp_list not in triplet_list:
                triplet_list.append(list())
                triplet_list[c].append(i)
                triplet_list[c].append(j)
                triplet_list[c].append(t)
                triplet_list[c].sort()
                c+=1
print(triplet_list)