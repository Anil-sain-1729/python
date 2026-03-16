# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(n-1):
        if(i%2==0):
            if(a[i]>a[i+1]):
                a[i],a[i+1] = a[i+1],a[i]
        else:
            if(a[i]<a[i+1]):
                a[i],a[i+1] = a[i+1],a[i]
                
    print(a)