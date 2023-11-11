import sys

input = sys.stdin.readline

n, q = map(int, input().split())
s = list(input())
s = s[:-1]
l = [0 for _ in range(q)]
r = [0 for _ in range(q)]

for i in range(q):
    l[i], r[i] = map(int, input().split())

same_count = [0] * n
count = 0
for i in range(n - 1):
    if s[i] == s[i + 1]:
        count += 1
    same_count[i] = count

for i in range(q):
    ans = same_count[r[i] - 2] - same_count[l[i] - 2]
    print(ans)
