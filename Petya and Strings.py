input1=list(input().lower())         
input2=list(input().lower())         
ret=0
length=len(input1)
for i in range(length):
    if input1[i]==input2[i]:
        continue
    elif input1[i]<input2[i]:
        ret=-1
        break
    elif input1[i]>input2[i]:  
        ret=1
        break

print(ret)
