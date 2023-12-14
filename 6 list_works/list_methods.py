# append() --- adding only one object to list 
# count() --- occurence of an object 
# index() --- return position
# pop() --- remove the last object from the list 
# pop(index) --- remove based on the index 
# inser(index,object) --- insert an object to any position
# remove() --- remove an object from the list
# copy() --- copy list 
# reverse() --- rotate the list

orders=["coffee","bread","rice","rice","coffee","rice"]
        #     0       1       2       3     4       5
        #    -6     -5      -4     -3      -2       -1

print("\nappend()")
orders.append("tea")
print(orders)

print("\ncount()")
print(orders.count("rice"))

print("\nindex()")
print(orders.index("bread"))

print("\npop()")
print(orders.pop())

print("\npop(index)")
print(orders.pop(-2))
print(orders)

print("\ninsert()")
orders.insert(1,"goby")
print(orders)

print("\nremove()")
orders.remove("bread")
print(orders)

print("\ncopy()")
mobin=["yellow","green","blue","red"]
manoj=mobin.copy()
manoj.remove("yellow")
print(manoj)
print(mobin)

print("\nreverse()")
mobin.reverse()
print(mobin)

print("\nsort()")
mobin.sort()
print(mobin)

print("\nsort(reverse)")
mobin.sort(reverse=True)
print(mobin)