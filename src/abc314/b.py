n = int(input())
c = [0 for _ in range(n + 1)]
dice = {}
for i in range(37):
    dice[i] = []

for i in range(1, n + 1):
    c[i] = int(input())
    a = list(map(int, input().split()))
    for item in a:
        dice[item].append(i)

x = int(input())

ans = []
min = 100
for item in dice[x]:
    if c[item] < min:
        ans = [item]
        min = c[item]
    elif c[item] == min:
        ans.append(item)
    else:
        pass

print(len(ans))
print(*ans)
