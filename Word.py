n=input()
upper=0
for i in n:
    if i.islower()!=True:
        upper+=1

if upper>len(n)-upper:
    print(n.upper())
else:
    print(n.lower())
