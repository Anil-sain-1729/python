a,b = map(int,input().split())
c = a-b
d = c%10
if d==9:
    x = 8
else:
    x = d+1
y = c-d+x
print(y)