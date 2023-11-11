import sys

input = sys.stdin.readline

s = input().rstrip()

result = []
for char in s:
    result.append(char)
    if len(result) >= 3 and result[-3:] == list("ABC"):
        result.pop()
        result.pop()
        result.pop()

print("".join(result))
