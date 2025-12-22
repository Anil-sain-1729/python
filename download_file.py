t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    e = 0
    for i in range(a):
        c, d = map(int, input().split())
        if(b>0):
            if(c<=b):
                b -= c
            else:
                e += (c - b) * d
                b = 0
        else:
            e += c*d
    print(e)