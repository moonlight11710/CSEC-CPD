n=int(input())
lis=[]
for i in range(n):
    i=input()
    lis.append(i)
counter=1
checker=lis[0]
for i in lis:
    if i==checker:
        continue
    else:
        counter+=1
        checker=i
print(counter)
