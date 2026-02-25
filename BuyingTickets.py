t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    s = input()
    
    se = []
    
    for i in range(n):
        if(s[i]=="0"):
            se.append(a[i])
            
    if(len(se)<k):
        print(-1)
    else:
        se.sort()
        print(sum(se[:k]))