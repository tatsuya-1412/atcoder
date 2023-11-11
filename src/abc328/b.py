import sys

input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))

ans = 0

for i in range(1, n + 1):
    for j in range(1, d[i - 1] + 1):
        is_same = True
        num = str(i) + str(j)
        for k in range(1, len(num)):
            if num[k] != num[0]:
                is_same = False
                break
        if is_same:
            ans += 1

print(ans)
