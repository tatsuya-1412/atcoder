n = int(input())
f = [0 for _ in range(n)]
s = [0 for _ in range(n)]

for i in range(n):
    fi, si = map(int, input().split())
    f[i] = fi
    s[i] = si

max_index = s.index(max(s))
max_f = f[max_index]
max_s = s[max_index]
ans = 0

for i in range(n):
    if i != max_index:
        tmp = 0
        if f[i] != max_f:
            tmp = max_s + s[i]
        else:
            tmp = max_s + int(s[i]/2)
        ans = max(ans, tmp)

print(ans)