n = int(input())
a = list(map(int, input().split()))

min = min(a)
max = max(a)
sum = sum(a)
sum_ap = int((n+1)*(min+max)/2)

ans = sum_ap - sum
print(ans)