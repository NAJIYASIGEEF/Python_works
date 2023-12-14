order1={"cb","tika","fishfry","friedrice","vb","gheeroast"}
order2={"cb","friedrice","nan","upma","vegmeals","idly"}

union_set=order1.union(order2)
intersection=order1.intersection(order2)
diff=union_set.difference(intersection)
print(diff)


# symmetric_difference

new_order=order1.symmetric_difference(order2)
print(new_order)


st1={10,20,30}
st2={100,200,300}
st1.update(st2)
print(st1)