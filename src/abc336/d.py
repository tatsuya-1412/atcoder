import sys

input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))

l = [0] * (n + 2)
r = [0] * (n + 2)
for i in range(1, n + 1):
    l[i] = min(a[i], l[i - 1] + 1)
for i in range(n, 0, -1):
    r[i] = min(a[i], r[i + 1] + 1)

print(max(min(l[i], r[i]) for i in range(1, n + 1)))
