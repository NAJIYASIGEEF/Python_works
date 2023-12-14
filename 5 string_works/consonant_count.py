#consonants

text="#@12pneumonoultramicroscopicsilicovolcanoconiosis"

c_count=0
for ch in text:
    if ch not in ["a","e","i","o","u"]:            # for printing characters other than vowels
        if ch.isalpha():                           # check whether the characters are alphabets
            c_count+=1
print(f"Vowel count= {c_count}")
print(f"Total no.of characters= {len(text)}")