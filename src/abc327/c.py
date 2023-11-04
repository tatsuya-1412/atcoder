import sys

input = sys.stdin.readline

a = [[0 for _ in range(9)] for _ in range(9)]

for i in range(9):
    a[i] = list(map(int, input().split()))

c = [0] * 10
ans = "Yes"

for i in range(9):
    c = [0] * 10
    if ans == "No":
        break
    for j in range(9):
        n = a[i][j]
        if c[n] == 1:
            ans = "No"
            break
        c[n] += 1

for j in range(9):
    c = [0] * 10
    if ans == "No":
        break
    for i in range(9):
        n = a[i][j]
        if c[n] == 1:
            ans = "No"
            break
        c[n] += 1

for i in range(3):
    if ans == "No":
        break
    for j in range(3):
        c = [0] * 10
        if ans == "No":
            break
        for k in range(3):
            for l in range(3):
                n = a[3 * i + k][3 * j + l]
                if c[n] == 1:
                    ans = "No"
                    break
                c[n] += 1

print(ans)
