import sys

input = sys.stdin.readline

s = list(input())
t = list(input())

edge_s = abs(ord(s[0]) - ord(s[1]))
edge_t = abs(ord(t[0]) - ord(t[1]))

if edge_s == 3:
    edge_s = 2
elif edge_s == 4:
    edge_s = 1

if edge_t == 3:
    edge_t = 2
elif edge_t == 4:
    edge_t = 1

if edge_s == edge_t:
    print("Yes")
else:
    print("No")
