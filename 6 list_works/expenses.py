expenses=[10000,12000,23000,22000,14000,24000,30000,15000]

# for i in range(0,len(expenses)):
#     print(expenses[i])

print(  "All expenses")
for exp in expenses:
    print(exp)

# print all expenses>15000
print("\nExpenses > 15k ")

for i in range(0,len(expenses)):
    if expenses[i]>15000:
        print(expenses[i])

print("\nExpenses b/w 15k and 25k")

# for i in range(0,len(expenses)):
#     if expenses[i]>15000 and expenses[i]<25000:
#         print(expenses[i])


for i in range(0,len(expenses)):
    if expenses[i] in range(15000,25000):
        print(expenses[i])

# Max expenses
print("\ncostly expenses")
max_exp=max(expenses)
print(max_exp)

# Min expenses
print("\nMinimum expenses")
min_exp=max(expenses)
print(min_exp)

# Total expenses
print("\nSum of expenses")
total_exp=sum(expenses)
print(total_exp)

# Average of expenses
avg=total_exp/len(expenses)
print(f"\nAverage ={avg}")

# print based on alphabetic order
print("\nAlphabetic order")
items=["bat","ball","stumps","helmet","arc","cricketball"]
word=max(items)
print(word)

# longest word
print("\n------longest word----------")
longest_word=max(items,key=lambda w:len(w))
print(longest_word)

#smallest word
print("\n--------smallest word---------")
small_word=min(items,key=lambda w:len(w))
print(small_word)

# sum of items



