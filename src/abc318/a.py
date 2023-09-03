N, M, P = map(int, input().split())

i = 0
cnt = 0
while True:
    if M + i * P > N:
        break
    cnt += 1
    i += 1

print(cnt)
