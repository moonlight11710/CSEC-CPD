n=int(input())
lis=list(map(int, input().split()))
m=int(input())
for i in range(m):
    k,l=map(int, input().split())
    if len(lis)==1:
        lis[k-1]=0
    elif k!=1 and k!=len(lis):
        lis[k-2]+=l-1
        lis[k]+=(lis[k-1]-l)
        lis[k-1]=0
        
    elif k==1:
        lis[k]+=lis[k-1]-l
        lis[k-1]=0
    elif k==len(lis):
        lis[k-2]+=l-1
        lis[k-1]=0

for i in lis:
    print(i)
