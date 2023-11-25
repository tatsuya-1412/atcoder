import sys

input = sys.stdin.readline

n, l, r = map(int, input().split())
a = list(map(int, input().split()))

ans = [r] * n

mid = (l + r) / 2

for i in range(n):
    if a[i] <= mid:
        ans[i] = l
    if l < a[i] < r:
        ans[i] = a[i]

print(*ans)
