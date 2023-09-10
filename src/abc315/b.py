m = int(input())
d = list(map(int, input().split()))

mid = int((sum(d)+1)/2)

tmp = 0
ans_month = 0
ans_order = 0
for (idx, di) in enumerate(d):
    if tmp+di >= mid:
        ans_order = mid - tmp
        ans_month = idx + 1
        break
    tmp += di

print(ans_month,ans_order)