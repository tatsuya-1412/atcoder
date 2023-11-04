import sys

input = sys.stdin.readline


n = int(input())
s = list(input())

is_a = False
is_b = False
ans = "No"
for si in s:
    if is_a and is_b:
        ans = "Yes"
    if si == "a":
        is_a = True
    elif si == "b":
        is_b = True
    else:
        is_a = False
        is_b = False

print(ans)
