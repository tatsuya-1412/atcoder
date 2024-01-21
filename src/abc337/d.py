import sys

input = sys.stdin.readline

h, w, k = map(int, input().split())
s = [[] for _ in range(h)]
for i in range(h):
    s[i] = list(input()[:-1])

ans = k + 1
for i in range(h):
    cnt = 0
    dot = 0
    tmp = k + 1
    for j in range(w):
        if s[i][j] == "x":
            cnt = 0
            dot = 0
            continue

        if s[i][j] == ".":
            dot += 1
        if cnt < k:
            cnt += 1
        else:
            if s[i][j - k] == ".":
                dot -= 1

        if cnt == k:
            tmp = min(tmp, dot)
    ans = min(ans, tmp)

for j in range(w):
    cnt = 0
    dot = 0
    tmp = k + 1
    for i in range(h):
        if s[i][j] == "x":
            cnt = 0
            dot = 0
            continue

        if s[i][j] == ".":
            dot += 1
        if cnt < k:
            cnt += 1
        else:
            if s[i - k][j] == ".":
                dot -= 1

        if cnt == k:
            tmp = min(tmp, dot)
    ans = min(ans, tmp)

if ans == k + 1:
    print(-1)
else:
    print(ans)
