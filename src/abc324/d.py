import sys

input = sys.stdin.readline
n = int(input())
s = list(input())
s.pop()
s = list(map(int, s))

cnt = [0] * 10
for si in s:
    cnt[si] += 1
min_d = n - cnt[0]

ans = 0
for i in range(4 * 10**6):
    num = i**2
    if len(str(num)) < min_d:
        continue
    if len(str(num)) > n:
        break
    cnt_s = [0] * 10
    flag = True
    for si in list(str(num)):
        cnt_s[int(si)] += 1
    for i in range(1, 10):
        if cnt[i] != cnt_s[i]:
            flag = False
            break
    if flag:
        ans += 1
print(ans)
