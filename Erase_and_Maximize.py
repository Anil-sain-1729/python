t = int(input())
for _ in range(t):
    n,s = map(int,input().split())
    
    if(s<=5*n):
        print(6*n)
    else:
        print(6*n-(s-5*n))