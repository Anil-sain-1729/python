t = int(input())
for _ in range(t):
    a,b,x,y = map(int,input().split())
    
    c = a//x 
    
    total = a+b+c*(y-x)
    print(total)