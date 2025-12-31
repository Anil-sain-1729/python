def solve(arr):
    n = len(arr)

    mn = [[0]*n for _ in range(n)]
    mx = [[0]*n for _ in range(n)]

    for i in range(n):
        mn[i][i] = arr[i]
        mx[i][i] = arr[i]

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            mn[i][j] = 10**18
            mx[i][j] = -10**18

            for k in range(i, j):
                mn[i][j] = min(mn[i][j], mn[i][k] + 2*mn[k+1][j])
                mx[i][j] = max(mx[i][j], mx[i][k] + 2*mx[k+1][j])

    return mn[0][n-1], mx[0][n-1]

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(A)
    print(ans[0], ans[1])
