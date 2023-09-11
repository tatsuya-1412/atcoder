# import io
# import sys

# # input here
# _INPUT = """\
# 8 3
# apzbqrcs
# 1 2 3 1 2 2 1 2
# """
# sys.stdin = io.StringIO(_INPUT)

n, m = map(int, input().split())
s = input()
c = list(map(int, input().split()))

p = {}
for i in range(m + 1):
    p[i] = []

for i, item in enumerate(c):
    p[item].append(i)

ans = ["*" for _ in range(n)]

for i in range(1, m + 1):
    for j, pi in enumerate(p[i]):
        if j == len(p[i]) - 1:
            ans[p[i][0]] = s[pi]
        else:
            ans[p[i][j + 1]] = s[pi]

print(*ans, sep="")
