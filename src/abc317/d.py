import sys

n = int(input())
x = [0 for _ in range(n)]
y = [0 for _ in range(n)]
z = [0 for _ in range(n)]
c = [0 for _ in range(n)]
t_sum = 0
z_sum = 0

for i in range(n):
    xi, yi, zi = map(int, input().split())
    x[i] = xi
    y[i] = yi
    z[i] = zi
    if xi > yi:
        c[i] = 0
        t_sum += zi
    else:
        c[i] = int((yi - xi + 1)/2)
    z_sum += zi

dp = [sys.maxsize for _ in range(z_sum+1)]
dp[0] = 0

for i in range(n):
    for j in range(z_sum, z[i]-1, -1):
        dp[j] = min(dp[j], dp[j -z[i]] + c[i])

ans = sys.maxsize
for i in range(int(z_sum/2) + 1, z_sum+1):
    ans = min(ans, dp[i])

print(ans)
