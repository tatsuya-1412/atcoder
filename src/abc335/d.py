import sys

input = sys.stdin.readline

n = int(input())

ans = [["" for _ in range(n)] for _ in range(n)]

ans[n // 2][n // 2] = "T"

pos = [0, 0]
d = "R"
directions = ["R", "D", "L", "U"]

a = [n - 1]
for i in range(n - 1, 1, -1):
    a.append(i)
    a.append(i)
a.append(1)

cnt = 1
ans[0][0] = cnt
cnt += 1

for i, ai in enumerate(a):
    d = directions[i % 4]
    for j in range(ai):
        if d == "R":
            pos[1] += 1
        elif d == "D":
            pos[0] += 1
        elif d == "L":
            pos[1] -= 1
        elif d == "U":
            pos[0] -= 1
        ans[pos[0]][pos[1]] = cnt
        cnt += 1

for ans_i in ans:
    print(*ans_i)
