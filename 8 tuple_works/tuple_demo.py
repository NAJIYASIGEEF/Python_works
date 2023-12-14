# TUPLE ()
# intertion order preserved
# duplictes allowed
# cannot be updated (immutable)
# should use , after the elements in tuple if there is only one element
# methods ---- count() ,index()

tp=(10,20,30,40,50,20)          
print(type(tp))
print(tp)                       #duplicates are allowed

# tp[0]=100
# print(tp)                     #updates not allowed

color1=("red")
print(type(color1))

color=("red",)                  #use comma if there is only on element
print(type(color))


tp1=(10,20,30,40,50,10,10)
print(tp1.count(10))            #count()

print(tp1.index(20))            #index()