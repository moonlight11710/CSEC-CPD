inp=input()
checker=[]
for i in range(len(inp)):
    if inp[i] in checker:
        continue
    else:
        checker.append(inp[i])

if len(checker)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
