import sys

input = sys.stdin.readline

s = input()
ans = True
for i in range(len(s) - 2):
    if s[i] == "B" and s[i + 1] == "A":
        ans = False
        break
    if s[i] == "C" and (s[i + 1] == "A" or s[i + 1] == "B"):
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")
