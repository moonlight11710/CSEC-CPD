n=int(input())
lis=[]
group=1
for i in range(n):
    row=list(input().split())
    lis.append(row)

for i in range(n-1):
    checker=lis[i]
    if lis[i]==lis[i+1]:
        continue
    else:
        group+=1

print(group)


