# set methods

#add()

colors={"red","green","blue"}
colors.add("yellow")
# print(colors)


# intersection
color1={"red","green","blue"}
color2={"blue","purple","yellow"}
inter_set=color1.intersection(color2)
# print(inter_set)

# union
union_set=color1.union(color2)
# print(union_set)

# difference
diff_set=color1.difference(color2)
# print(diff_set)
diffference_set=color2.difference(color1)
# print(diffference_set)

#pop
color1.pop()            #remove from first oject 
# print(color1)


# remove
st1={"red","green","blue"}
st1.remove("red")
# print(st1)

# discard
st1.discard("red")
# print(st1)

# st1.remove("reds")    #shows error
st1.discard("reds")     #only discards
# print("Hello")

