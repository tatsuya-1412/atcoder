import sys

input = sys.stdin.readline

n, q = map(int, input().split())
r = list(map(int, input().split()))

r.sort()

sum = [0] * (n + 1)

for i in range(1, n + 1):
    sum[i] += sum[i - 1] + r[i - 1]

for _ in range(q):
    x = int(input())

    left = 0
    right = n
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if sum[mid] == x:
            ans = mid
            break
        elif sum[mid] < x:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1

    print(ans)
