n = int(input())
d = [[0 for _ in range(n)] for _ in range(n)]
dp = [0] * (1 << n)

for i in range(n-1):
    line = list(map(int, input().split()))
    for j in range(i+1, n):
        d[i][j] = line[j - i - 1]

for b in range((1 << n) - 1):
    l = -1
    for i in range(n):
        if not (b >> i & 1):
            l = i
            break
    
    for i in range(n):
        if not (b >> i & 1):
            nb = b | (1 << l) | (1 << i)
            dp[nb] = max(dp[nb], dp[b] + d[l][i])

print(dp[-1])