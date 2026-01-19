n = int(input())
a = list(map(int,input().split()))

m = 0
c = 0

for i in a:
    if i == 0:
        m = max(m,c)
        c = 0
    else:
        c += 1
    
m = max(m,c)
print(m)
    
