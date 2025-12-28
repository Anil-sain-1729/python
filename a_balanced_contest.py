t = int(input())
for _ in range(t):
    n,p = map(int,input().split())
    l = list(map(int,input().split()))
    
    c = 0
    d = 0
    for i in l:
        if(i<=p//10):
            c += 1
        elif(i>=p//2):
            d += 1
    if(c == 2 and d == 1):
        print("YES")
    else:
        print("NO")