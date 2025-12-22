t = int(input())
for _ in range(t):
    a,b,c,d = map(int,input().split())
    if((a+b)%2==(c+d)%2):
        print("yes")
    else:
        print("no")