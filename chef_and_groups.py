t = int(input())
for _ in range(t):
    s = input()
    c = 0
    for i in range(len(s)):
        if s[i] == '1' and (i == 0 or s[i-1] == '0'):
            c += 1
    print(c)
