t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    b.sort()
    
    ok = True
    for i in range(n):
        if b[i] < i + 1:
            ok = False
            break
    
    print("Yes" if ok else "No")