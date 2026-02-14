n=int(input())
lis=list(map(int, input().split()))
sereja=0
dima=0
while len(lis)!=0:
    sereja+=max(lis[0],lis[-1])
    lis.remove(max(lis[0],lis[-1]))
    if len(lis)==0:
        break
    dima+=max(lis[0],lis[-1])
    lis.remove(max(lis[0],lis[-1]))
print(sereja, dima)
