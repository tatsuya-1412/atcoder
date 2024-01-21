import sys

input = sys.stdin.readline

n = int(input())

ans = 0
n_bin = format(n, "b")
for i in range(len(n_bin)):
    if n_bin[len(n_bin) - i - 1] == "1":
        break
    ans += 1

print(ans)
