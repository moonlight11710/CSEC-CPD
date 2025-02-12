amount, r = map(int, input().split())
for i in range(1, 11):
    if amount * i % 10 == r or amount * i % 10 == 0:
        print(i)
        break
