n=int(input())
lis=input()
counter=0

for i in range(n):
    if len(lis)==0 or len(lis)== 1:
        break
    elif lis[0]==lis[1]:
        counter+=1
        lis=lis[1:]
    else:
        lis=lis[1:]
print(counter)
