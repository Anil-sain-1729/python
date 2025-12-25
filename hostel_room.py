t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    s = list(map(int, input().split()))
    
    c = [0 for i in range(n+1)]
    c[0] = x

    for i in range(1,n+1):
        c[i] = s[i-1]+c[i-1]
    print(max(c))
