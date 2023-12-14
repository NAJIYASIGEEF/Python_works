# 2. Write a python program to make combinations of 3 digits
combinations = []

for digit1 in range(0,10):
    for digit2 in range(0,10):
        for digit3 in range(0,10):
            combination = digit1 * 100 + digit2 * 10 + digit3
            if combination >=100 and combination < 1000:
                combinations.append(combination)

print(combinations) 


