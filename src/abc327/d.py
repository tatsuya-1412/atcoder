# import io
# import sys

# # input here
# _INPUT = """\
# 3 2
# 1 2
# 2 3
# """
# sys.stdin = io.StringIO(_INPUT)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = "Yes"
x = [set() for _ in range(n + 1)]
for i in range(m):
    if a[i] < b[i]:
        x[a[i]].add(b[i])
    elif a[i] > b[i]:
        x[b[i]].add(a[i])
    else:
        ans = "No"
        break

if ans == "Yes":
    for i in range(n + 1):
        if ans == "No":
            break
        if not x[i]:
            continue
        for si in x[i]:
            for sj in x[si]:
                if sj in x[i]:
                    ans = "No"

print(ans)
