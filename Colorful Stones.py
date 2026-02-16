n=input()
t=input()
position=0
for i in range(len(t)):
    if t[i]==n[position]:
        position+=1
print(position+1)
