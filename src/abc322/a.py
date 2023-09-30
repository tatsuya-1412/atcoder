n = int(input())
s = input()

ans = s.find("ABC") + 1

if not ans:
    ans = -1

print(ans)
