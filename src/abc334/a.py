import sys

input = sys.stdin.readline

b, g = map(int, input().split())

if b > g:
    print("Bat")
else:
    print("Glove")
