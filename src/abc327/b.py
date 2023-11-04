import sys

input = sys.stdin.readline

b = int(input())

ans = -1
for i in range(1, 16):
    if b == i**i:
        ans = i

print(ans)
