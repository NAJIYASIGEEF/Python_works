# 4.Pattern print 
#         A 
#        B C 
#       D E F 
#      G H I J 
#     K L M N O

i=65
for row in range(1,7):
    for col in range(1,7-row):
        print(end=" ")
    for col2 in range(1,row+1):
        print(chr(i),end=" ")
        i+=1
    print("  ")
