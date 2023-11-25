import math
import sys

input = sys.stdin.readline

d = int(input())

sqrt_d = int(math.sqrt(d))
ans = d

for x in range(0, sqrt_d + 1):
    tmp = abs(x**2 - d)
    sqrt_y = int(math.sqrt(tmp))

    ans1 = abs(x**2 + sqrt_y**2 - d)
    if ans1 < ans:
        ans = ans1

    ans2 = abs(x**2 + (sqrt_y + 1) ** 2 - d)
    if ans2 < ans:
        ans = ans2

    if ans == 0:
        break

print(ans)
