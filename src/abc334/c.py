import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
if k % 2 == 0:
    for i in range(0, k, 2):
        ans += a[i + 1] - a[i]
elif k == 1:
    ans = 0
else:
    diff = [0] * (k - 1)
    for i in range(0, k - 1):
        diff[i] = a[i + 1] - a[i]

    ans = 0
    sum = 0
    for i in range(1, k - 1, 2):
        sum += diff[i]
    ans = sum

    for i in range(0, k - 2, 2):
        sum += diff[i] - diff[i + 1]
        if sum < ans:
            ans = sum

print(ans)
