n, m = map(int, input().split())
s = input()
t = input()

prefix = t.find(s)
suffix = t.rfind(s)

ans = -1
if prefix == 0 and suffix == m - n:
    ans = 0
elif prefix == 0:
    ans = 1
elif suffix == m - n:
    ans = 2
else:
    ans = 3

print(ans)
