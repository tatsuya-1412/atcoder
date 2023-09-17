s = list(input())
ans = 0

for i in range(len(s)):
    left = i
    right = i
    while True:
        if left == -1 or right == len(s) or s[left] != s[right]:
            break
        left -= 1
        right += 1
    ans = max(ans, right - left - 1)

for i in range(len(s)):
    left = i
    right = i + 1
    while True:
        if left == -1 or right == len(s) or s[left] != s[right]:
            break
        left -= 1
        right += 1
    ans = max(ans, right - left - 1)

print(ans)
