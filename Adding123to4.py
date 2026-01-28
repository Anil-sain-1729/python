t = int(input())
for _ in range(t):
    x,y,z = map(int,input().split())
    c = min(x,z)
    d = y//2
    print(c+d)