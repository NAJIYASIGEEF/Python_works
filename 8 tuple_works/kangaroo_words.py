source_word="myself"
target_word="selfn"

source_word_list=[ch for ch in source_word]
print(source_word_list)

target_word_list=[ch for ch in target_word]
print(target_word_list)

for ch in target_word_list:
    if ch in source_word_list:
        source_word_list.remove(ch)
    else:
        print("Not kangaroo word")
        break
else:
    print("kangaroo word")