import sys

input = sys.stdin.readline

n = int(input())
s = ["" for _ in range(n)]
for i in range(n):
    s[i] = list(input())[:-1]

r = [0] * n
c = [0] * n

for i in range(n):
    cnt_r = 0
    cnt_c = 0
    for j in range(n):
        if s[i][j] == "o":
            cnt_r += 1
        if s[j][i] == "o":
            cnt_c += 1
    r[i] = cnt_r
    c[i] = cnt_c

ans = 0
for i in range(n):
    for j in range(n):
        if s[i][j] == "o":
            ans += (r[i] - 1) * (c[j] - 1)

print(ans)
