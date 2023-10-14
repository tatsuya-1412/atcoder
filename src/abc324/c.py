import sys

input = sys.stdin.readline

n, st = input().split()
n = int(n)
st = list(st)

ans = []
for i in range(n):
    s = list(input())
    s.pop()

    cnt = 0
    flag = True
    if len(s) == len(st):
        for j in range(len(s)):
            if s[j] != st[j]:
                cnt += 1
            if cnt > 1:
                flag = False
                break
    elif len(s) == len(st) + 1:
        j = 0
        jj = 0
        while j < len(st):
            if s[jj] != st[j]:
                cnt += 1
                j -= 1
            if cnt > 1:
                flag = False
                break
            j += 1
            jj += 1
    elif len(s) == len(st) - 1:
        j = 0
        jj = 0
        while j < len(s):
            if s[j] != st[jj]:
                cnt += 1
                j -= 1
            if cnt > 1:
                flag = False
                break
            j += 1
            jj += 1
    else:
        continue
    if flag:
        ans.append(i + 1)

print(len(ans))
print(*ans)
