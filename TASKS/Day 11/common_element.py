# 1. Write a Python program that print 2 list and common element

lst1=[2,3,5,1,7,3]
lst2=[2,6,7,8,9,1]

set1=set()
set1.update(lst1)
print(f"list 1 : {set1}")
set2=set()
set2.update(lst2)
print(f"list 2 : {set2}")
common_element=list(set1.intersection(set2))
print(f"Common element: {common_element}")







# lst=[]
# lst.append(common_element)
# print(lst)