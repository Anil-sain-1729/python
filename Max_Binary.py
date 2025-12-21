t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = list(input())  
    
    if s[0] == '0' and k > 0:
        s[0] = '1'  
        k -= 1
    
    s += ['0'] * k  
    print("".join(s))  