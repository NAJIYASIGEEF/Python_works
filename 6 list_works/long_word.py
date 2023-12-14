# find longest word from given list witout using builtin functions
words=["hi","good","morning","all","hello"]
max_word=words[0]

for i in range(1,len(words)):
    current_word=words[i]
    if len(current_word)>len(max_word):
        max_word=current_word
print(max_word)

max_word=max(words,key=lambda w:len(w))


# min
# sum