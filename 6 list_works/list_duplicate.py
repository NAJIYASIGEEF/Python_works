arr=[4,9,5,6,9,5,4]
arr.sort()
# print(arr)
# for i in range(0,len(arr)-1):
#     for j in range(i+1,len(arr)):
#         i_element=arr[i]
#         j_element=arr[j]
#         diff=j_element-i_element
#         if diff==0:
#             print(i_element)
#             break

i=0
while(i<len(arr)-1):
    j=i+1
    i_element=arr[i]
    j_element=arr[j]   
    diff=j_element-i_element
    if diff==0:
        print(i_element)
        i=j
    i+=1
    

    # arr=[1,4,3,5,6,7]
    # missing +ve integer

    # sort#
    # diff==1#

        