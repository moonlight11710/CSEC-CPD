n=int(input())
counter=0
matrix= []
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
    
for j in matrix:
    if j[0]+j[1]+j[2] >=2:
        counter+=1
print(counter)
