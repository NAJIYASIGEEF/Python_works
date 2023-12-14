#        3. Pattern print 
#            1 1 1 1 1 1 1
#            2 2 2 2 2 2
#            3 3 3 3 3 
#            4 4 4 4 
#            5 5 5
#            6 6
#            7
  
for row in range(1,8):
    for col in range(7-row+1):
        print(row,end=" ")
    print(" ")
