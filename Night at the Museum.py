one = list(map(str, "abcdefghijklmnopqrstuvwxyz"))

word = input()
step = 0
current = 0

for i in range(len(word)):
    target = one.index(word[i])
    direct_distance = abs(target - current)
    wrap_around_distance = 26 - direct_distance
    
    step += min(direct_distance, wrap_around_distance)
    current = target

print(step)
        
