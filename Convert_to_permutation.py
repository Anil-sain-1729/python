t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    
    l.sort()
    
    a = 0
    p = True
    
    for i in range(n):
        if l[i]>i+1:
            p = False
            break
        a += (i+1)-l[i]

    if not p:
        print(-1)
    else:
        print(a)