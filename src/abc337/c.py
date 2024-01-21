# import io
# import sys

# # input here
# _INPUT = """\
# 6
# 4 1 -1 5 3 2
# """
# sys.stdin = io.StringIO(_INPUT)

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
ans = []

from collections import defaultdict

d = defaultdict(int)

for i in range(n):
    d[a[i]] = i + 1
# print(d)

s = d[-1]
ans.append(s)

for _ in range(n - 1):
    s = d[s]
    ans.append(s)

print(*ans)
