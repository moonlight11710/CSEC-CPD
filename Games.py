n=int(input())
liss=[]
numberofgames=n*(n-1)
counter=0

for i in range(n):
    lis=list(map(int,input().split()))
    liss.append(lis)

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        elif liss[i][0]==liss[j][1]:
            counter+=1
            
print(counter)
