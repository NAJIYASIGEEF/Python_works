#anagram

source_word="won"
target_word="now"

srt_source=sorted(source_word)
print(srt_source)

srt_target=sorted(target_word)
print(srt_target)


print("True" if srt_source==srt_target else "False")

# if srt_source==srt_target:
#     print("Anagram")
# else:
#     print("not")