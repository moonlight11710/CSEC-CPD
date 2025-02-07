word=input()
upper=0
lower=0
for i in word:
    if i.lower()==i:
        lower+=1
    else:
        upper+=1
if lower>=upper:
    print(word.lower())
else:
    print(word.upper())
