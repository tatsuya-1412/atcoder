n, h, x = map(int, input().split())
p = list(map(int, input().split()))

for i, pi in enumerate(p, start=1):
    if h+pi >=x:
        print(i)
        break