from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))

da = deque(a)
s = [0] * n
tmp = -1
for i in range(n):
    if (i + 1) > tmp:
        tmp = da.popleft()
    s[i] = tmp - (i + 1)

for v in s:
    print(v)
