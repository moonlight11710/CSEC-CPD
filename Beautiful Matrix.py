matrix=[]
for i in range(5):
    row=list(map(int,input().split()))
    matrix.append(row)


for i in matrix:
    for j in i:
        if j==1:
            print(abs(3-(matrix.index(i)+1))+abs(3-(i.index(j)+1)))
            break
          
    
