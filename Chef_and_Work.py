def anil():
    n,k = map(int,input().split())
    w = list(map(int,input().split()))
    
    tr = 0
    c = 0
    
    for wr in w:
        if wr>k:
            print(-1)
            return
        
        if c + wr <= k:
            c += wr
        else:
            tr += 1 
            c = wr
    if c > 0:
        tr += 1 
    
    print(tr)
    
t = int(input())
for _ in range(t):
    anil()