lst=[10,12,4,8,9]

lst.sort()
element=int(input("Enter number: "))
is_present=False
low=0
upper=len(lst)-1


while(low<=upper):
    mid=(low+upper)//2
    if element==lst[mid]:
        is_present=True
        break

    elif element<lst[mid]:
        upper=mid-1

    elif element>lst[mid]:
        low=mid+1

print(is_present)


