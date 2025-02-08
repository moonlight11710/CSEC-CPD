n=list(map(int,input().split()))
turns=list(map(int,input()))
calories=0

for i in turns:
    if i==1:
        calories+=n[0]
    elif i==2:
        calories+=n[1]
    elif i==3:
        calories+=n[2]
    elif i==4:
        calories+=n[3]
print(calories)

