

lst=[10,2,11,5,7,20]
element=int(input("Enter number:"))

is_present=False
for i in range(0,len(lst)):
    current_element=lst[i]
    if current_element==element:
        is_present=True
        break
print(is_present)
