words=["hi","good","morning"]
min_words=words[0]

for i in range(0,len(words)):
    current_word=words[i]
    if len(current_word)<len(min_words):
        min_words=current_word
print(min_words)

min_words=min(words,key=lambda w:len(w))
