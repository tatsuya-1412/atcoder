n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = -1

a_min = min(a)
a_max = max(a)

a_sum = sum(a)

a_sum_exclude = a_sum - a_min - a_max

tmp = x - a_sum_exclude

if a_min < tmp < a_max:
    ans = tmp
elif tmp == a_min and tmp == a_max:
    ans = 0
elif tmp == a_min:
    ans = 0
elif tmp == a_max:
    ans = tmp
elif tmp < a_max:
    ans = 0

print(ans)
