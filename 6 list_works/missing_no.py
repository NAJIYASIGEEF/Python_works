# find missing positive integer
arr=[1,4,3,5,6,7]
arr.sort()
print(arr)
i=0
while(i<len(arr)-1):
    j=i+1
    i_element=arr[i]
    j_element=arr[j]
    diff=j_element-i_element
    if diff!=1:
        print(i_element+1)
        i=j
    i+=1
    


