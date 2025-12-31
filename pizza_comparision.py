t =int(input())
for _ in range(t):
    a,b = map(int,input().split())
    c = a/100
    d = b/225
    if(c<d):
        print("Small")
    elif(c>d):
        print("Large")
    else:
        print("Equal")