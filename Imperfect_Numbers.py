t = int(input())
for _ in range(t):
    n = int(input())
    if(n%10==0):
        print(2)
    elif(n%2==0):
        print(0)
    elif(n%5==0):
        print(0)
    else:
        print(1)