dengue_list=["ekm","ekm","tsr","tvm","tvm","ekm","tvm","idk","tvm"]

wc={}

for dis in dengue_list:
    if dis in wc:
        wc[dis]+=1   
    else:
        wc[dis]=1
# print(wc)

srt_wc=sorted(wc,key=lambda k:wc.get(k),reverse=True)
print(srt_wc)