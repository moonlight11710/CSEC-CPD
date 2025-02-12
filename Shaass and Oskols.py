n = int(input())
birds = list(map(int, input().split()))
m = int(input())
shots = []

for _ in range(m):
    x, y = map(int, input().split())
    shots.append((x, y)) 
     
def shoot_birds(n, birds, shots):
    for x, y in shots:
        x -= 1  
        left, right = x - 1, x + 1

        if left >= 0:
            birds[left] += y - 1 
        if right < n:
            birds[right] += birds[x] - y  

        birds[x] = 0

    return birds

for count in shoot_birds(n, birds, shots):
    print(count)
