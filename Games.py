n=int(input())
home=[]
away=[]
answer=0
for i in range(n):
    row=list(map(int, input().split()))
    home.append(row[0])
    away.append(row[1])
for i in range(n):
    for j in range(n):
        if home[i]==away[j]:
            answer+=1
print(answer)
