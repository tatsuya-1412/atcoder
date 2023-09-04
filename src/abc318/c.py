from math import ceil

n, d, p = map(int, input().split())
f = list(map(int, input().split()))
s = [0 for _ in range(n)]

f_s = sorted(f)

s[0] = f_s[0]
for i in range(n-1):
    s[i+1] = s[i] + f_s[i+1]

k = ceil(n/d)
cost = k*p
for i in range(k):
    cost = min(cost, i*p+s[n-1-i*d])
print(cost)