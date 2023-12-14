# 3.Pattern print
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3 
# 4 4  
# 5

for row in range(1,6):
    for col in range(1,7-row):
        print(row,end=" ")
    print("")
