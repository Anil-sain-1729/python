def anil():
    n = int(input())
    if n == 3:
        print("3 2 1")
        return
    
    r = [n,n-2]+list(range(1,n-2))+[n-1]
    print(*r)
    
t = int(input())
for _ in range(t):
    
    anil()