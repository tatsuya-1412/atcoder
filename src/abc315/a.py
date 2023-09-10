s = list(input())
ans = ''

for si in s:
    if si != 'a' and si != 'i' and si != 'u' and si != 'e' and si != 'o':
        ans += si

print(ans)