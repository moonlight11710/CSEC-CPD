shoes=list(map(int,input().split()))
amount=[]
for i in shoes:
    if i not in amount:
        amount.append(i)
print(4-len(amount))
