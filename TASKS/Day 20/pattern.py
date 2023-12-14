# 3. Pattern print 
#                             4 4 4 4 4 4 4  
#                             4 3 3 3 3 3 4   
#                             4 3 2 2 2 3 4   
#                             4 3 2 1 2 3 4   
#                             4 3 2 2 2 3 4   
#                             4 3 3 3 3 3 4   
#                             4 4 4 4 4 4 4

n=4
for row in range(1,2*n):
    for col in range(1,2*n):
        print(max(row-3,col-3,2*n-row-3,2*n-col-3),end=" ")
    print()



