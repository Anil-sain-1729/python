t = int(input())
for _ in range(t):
    n = int(input())
    c = n%8
    if c==1:
        print(str(n+3)+"LB")
    elif c==2:
        print(str(n+3)+"MB")
    elif c==3:
        print(str(n+3)+"UB")
    elif c==4:
        print(str(n-3)+"LB")
    elif c==5:
        print(str(n-3)+"MB")
    elif c==6:
        print(str(n-3)+"UB")
    elif c==7:
        print(str(n+1)+"Su")
    elif c==0:
        print(str(n-1)+"SL")