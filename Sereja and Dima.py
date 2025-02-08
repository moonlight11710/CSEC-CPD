n=int(input())

lis=list(map(int,input().split()))

sereja=0
dema=0
checker=1

for i in range(n):
    if len(lis)==0:
        break
    elif len(lis)==1:
        if checker%2!=0:
            sereja+=lis[0]
        else:
            dema+=lis[0]
    elif lis[0]>lis[-1]:
        if checker%2!=0:
            sereja+=lis[0]
            checker+=1
            lis.remove(lis[0])
        else:
            dema+=lis[0]
            checker+=1
            lis.remove(lis[0])
    elif lis[0]<lis[-1]:
        if checker%2!=0:
            sereja+=lis[-1]
            checker+=1
            lis.remove(lis[-1])
        else:
            dema+=lis[-1]
            checker+=1
            lis.remove(lis[-1])
print(sereja, dema)
