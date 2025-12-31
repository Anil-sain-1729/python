t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    balance = 0
    good = 0

    for ch in s:
        if ch == '1':
            balance += 1
        else:
            balance -= 1

        if balance >= 0:
            good += 1

    print(good)
