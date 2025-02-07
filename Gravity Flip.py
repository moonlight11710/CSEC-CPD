c = int(input())

lis =  list(map(int, input().split()))

lis.sort()

for i in range(c):

    print(lis[i], "", end = "")
