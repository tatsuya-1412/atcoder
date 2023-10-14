import sys

input = sys.stdin.readline

n = int(input())

while True:
    if n % 2 != 0:
        break
    n /= 2

while True:
    if n % 3 != 0:
        break
    n /= 3

if n == 1:
    print("Yes")
else:
    print("No")
