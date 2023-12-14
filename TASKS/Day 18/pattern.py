#        3. Pattern print 
#       A 
#      A B 
#     A B C 
#    A B C D 
#   A B C D E
i=65
for row in range(1,6):
    for space in range(1,6-row):
        print(end=" ")
        
    for col in range(1,row+1):
        print(chr(i-1+col),end=" ")
        
    print(" ")