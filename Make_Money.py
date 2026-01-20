t = int(input())
for _ in range(t):
    n,x,c = map(int,input().split())
    a = list(map(int,input().split()))
    
    d = 0
    for i in a:
        if x-c>i:
            d += x-c
        else:
            d += i 
    
    print(d)