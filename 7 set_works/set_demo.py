# { }
# insertion irder preserved
# duplication not allowed
# 



st={}                       #dictionary
print(type(st))

st={10,20,30}               #set
print(type(st)) 

st=set( )                   #empty set
lst=[] or list()            #empty list
tp=() or tuple()            #empty tuple
dict={} or dict()           #empty dict

st={10,20,True,"hello"}     #insertion order not preserved
print(st)
# print(st[0]) ---- #indexing not supported

st1={10,20,True,"hello",10,20}      #duplication not allowed
print(st1)

