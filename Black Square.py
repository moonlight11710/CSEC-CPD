n=list(map(int, input().split()))
string=input()
calories=0
for i in string:
    calories+=n[int(i)-1]
print(calories)
