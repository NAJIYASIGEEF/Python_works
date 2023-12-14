# 2.Convert tuple to a list and find sum

tp=(12,10,4,4,10,5,5)

sum=0
sum_list=[]

tple=list(tp)
print(tple)

for i in tple:
    # print (i)
    sum=sum+i
print(f"sum of the elements : {sum}")
