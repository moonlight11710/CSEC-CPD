n=int(input())
lis=list(map(int,input().split()))
freePolice=0
crime=0
for i in range(n):
    if lis[i]==-1:
        if freePolice>0:
            freePolice-=1
        else:
            crime+=1
    else:
        freePolice+=lis[i]
print(crime)
