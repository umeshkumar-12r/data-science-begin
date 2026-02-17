words =["apple ", "rose","banana","guava"]
print(words)
newwords = [str.upper(x) for x in words]
upper_words = [w.upper() for w in words]


print(newwords,"\n",upper_words)