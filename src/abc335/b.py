import sys

input = sys.stdin.readline

n = int(input())

for i in range(n + 1):
    for j in range(n + 1 - i):
        for k in range(n + 1 - i - j):
            ans = [i, j, k]
            print(*ans)
