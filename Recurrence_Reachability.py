t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    found = False
    for x in range(1, n + 1):
        for y in range(x + 1, n + 1):
            
            a = x
            b = y
            if a == m or b == m:
                print(x, y)
                found = True
                break
            
            for _ in range(50):
                c = 3 * b - 2 * a
                if c == m:
                    print(x, y)
                    found = True
                    break
                
                if c > m:
                    break
                
                a, b = b, c
            
            if found:
                break
        
        if found:
            break
    
    if not found:
        print(-1)