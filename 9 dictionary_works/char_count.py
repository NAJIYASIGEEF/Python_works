text="good morning"

wc={}

for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
print(wc)



# text="hello hai hello hai"
# word count
# hello:2
# hello:2