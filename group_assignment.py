from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    g = list(map(int, input().split()))
    
    gcounts = Counter(g)
    
    possible = True
    for size, count in gcounts.items():
        if count % size != 0:
            possible = False
            break
            
    if possible:
        print("YES")
    else:
        print("NO")