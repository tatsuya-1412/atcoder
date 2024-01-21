import io
import sys

# input here
_INPUT = """\
3 3
##.
#.#
#..
"""
sys.stdin = io.StringIO(_INPUT)

# your code here
import sys

input = sys.stdin.readline

h, w = map(int, input().split())
s = [[] for _ in range(h)]

for i in range(h):
    s[i] = list(input())[:-1]

print(s)
