# RE---pattern matching

from re import *
text="az1cbyabcaA rBZesd9@"
pattern="\w"

matcher=finditer(pattern,text)
 
for m in matcher:
    print(m.start(),m.group())


# [ac]   matches a or c
# [abc]  matches a or b or c
# [a-e]  matches a to e
# [a-z]  matches lowercase a to z 
# [A-Z]  matches uppercase A to Z
# [a-zA-Z]  matches all alphabets
# [0-9]   matches all digits
# [a-zA-Z0-9]   matches all alphanumeric characters
# [^a-z]   matches all excluding alphabets
# [^a-zA-Z0-9]   matches special characters
# \d   matches digits(0-9)
# \D   exclusing digits
# \w   all alphanumeric(a-zA-Z0-9)
