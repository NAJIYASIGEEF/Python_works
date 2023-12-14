# 3.Pattern print 
#      * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     *

for row in range(1,6):
    for space in range(1,6-row):
        print(end=" ")
    for col in range(1,row+1):
        print("*",end=" ")
    print()

for row in range(5, 0, -1):
    for space in range(0, 5-row):
        print(end=" ")
    for column in range(0, row):
        print("*", end=" ")
    print()