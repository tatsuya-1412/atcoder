# N, D, P = map(int, input().split())
# F = list(map(int, input().split()))

# dp = [float("inf")] * (N + 1)
# dp[0] = 0

# for i in range(1, N + 1):
#     dp[i] = dp[i - 1] + F[i - 1]
#     for j in range(1, D + 1):
#         if i - j >= 0:
#             dp[i] = min(dp[i], dp[i - j] + P)

# print(dp[N])

N, D, P = map(int, input().split())
F = list(map(int, input().split()))

F_sorted = sorted(F, reverse=True)
cost = 0
pass_buy = 0

sum = 0
sum_l = 0
is_ordinary = False
flag = False
for i in range(N):
    flag = False
    sum += F_sorted[i]
    sum_l += F_sorted[i]
    if not is_ordinary:
        if (i + 1) % D == 0:
            if sum >= (pass_buy + 1) * P:
                pass_buy += 1
            else:
                is_ordinary = True
                cost += sum_l
            sum_l = 0
            flag = True
    if is_ordinary:
        cost += F_sorted[i]

if (not flag) and (not is_ordinary):
    if sum >= (pass_buy + 1) * P:
        pass_buy += 1
    else:
        cost += sum_l

for i in range(pass_buy):
    cost += P
print(cost)
