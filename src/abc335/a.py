import re
import sys

input = sys.stdin.readline

s = input()
ans = re.sub(r".$", "4", s)

print(ans)
