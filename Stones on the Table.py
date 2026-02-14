n=int(input())
word=input()
checker=word[0]
count=0
for i in range(1, len(word)):
    if word[i]==checker:
        count+=1
    else:
        checker=word[i]
print(count)

