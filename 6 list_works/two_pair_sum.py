
lst=[3,4,5,6,2]
sum=int(input("Enter sum= "))
lst.sort()

# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         cur_sum=lst[i]+lst[j]
#         if cur_sum==sum:
#             print(lst[i],lst[j])
#             break

lower=0
upper=len(lst)-1
while(lower<upper):
    curr_sum=lst[lower]+lst[upper]
    if curr_sum==sum:
        print(lst[lower],lst[upper])
        lower+=1
        upper-=1
    elif curr_sum<sum:
        lower+=1
    elif curr_sum>sum:
        upper-=1

