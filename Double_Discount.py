t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))  
    b = list(map(int,input().split()))  

    m = 0

    for i in range(n):
        for j in range(i + 1, n):
            c1, c2 = a[i],a[j]
            ta = b[i] + b[j]

            mx = max(c1, c2)
            mn = min(c1, c2)

            di = min(mx // 2, 100)
            total = mn + (mx - di)

            if total <= k:
                m = max(m, ta)
    print(m)