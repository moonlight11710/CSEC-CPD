seq=input()
instruction=input()
position=1
j=0
for i in range(len(instruction)):
    if instruction[i]==seq[j]:
        position+=1
        j+=1

    else:
        continue
print(position)
