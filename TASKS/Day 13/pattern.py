# 3.Pattern print 
# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1


for row in range(1,6):
    for col1 in range(1,row+1):
        print(col1,end=" ")
    for col2 in range(col1-1,0,-1):
        print(col2,end=" ")
    print("")