import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

flag = True
for ai in a:
    if ai != a[0]:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
