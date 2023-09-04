n, m, p = map(int, input().split())

i = 0
cnt = 0
while True:
    if m + i * p > n:
        break
    cnt += 1
    i += 1

print(cnt)
