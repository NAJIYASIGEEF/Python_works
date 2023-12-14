# first recursive character
text="ABCABBDE"
wc={}
for ch in text:
    if ch in wc:
        print(ch)
        break
    else:
        wc[ch]=1      





