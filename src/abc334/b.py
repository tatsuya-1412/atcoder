import sys

input = sys.stdin.readline

a, m, l, r = map(int, input().split())

ans = 1 + (r - a) // m + (a - l) // m

print(ans)
