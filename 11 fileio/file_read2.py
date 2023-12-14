f=open("D:\\Desktop\\Python works\\fileio\\news.txt","r")

count=0
wc={ }
for line in f:
    words=line.rstrip("\n").split(" ")
    print(words)
    for w in words:
        if w in wc:
            wc[w]+=1
        else:
            wc[w]=1
print(wc)














# total no.of characters in each word

# for line in f:
#     word=len(line.rstrip("\n"))
#     print(word)