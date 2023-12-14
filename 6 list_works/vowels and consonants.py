
# starting with vowels

lst = ["red", "green", "blue", "white", "apple", "ignore", "under"]
vowels = [vow for vow in lst if vow[0] in (("a","e","i","o","u"))]
print(vowels)

# starting with consosnants

# lst = ["red", "green", "blue", "white", "apple", "ignore", "under"]
# consonants=[word for word in lst if not word.startswith(("a","e","i","o","u"))]
# print(consonants)

lst = ["red", "green", "blue", "white", "apple", "ignore", "under"]
consonants=[word for word in lst if  word[0] not in (("a","e","i","o","u"))]
print(consonants)
