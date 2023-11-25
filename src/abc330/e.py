import sys

input = sys.stdin.readline

import heapq
from collections import defaultdict

input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))

que = list(range(n + 1))
heapq.heapify(que)
del_que = []

bk = defaultdict(int)


for i in range(n):
    if a[i] <= n:
        if bk[a[i]] == 0:
            heapq.heappush(del_que, a[i])
        bk[a[i]] += 1

print(del_que)
print(que)
for _ in range(q):
    i, x = map(int, input().split())
    i -= 1

    if a[i] <= n:
        bk[a[i]] -= 1
        if bk[a[i]] == 0:
            heapq.heappush(que, a[i])
    print(a[i])
    print(que)

    a[i] = x

    if a[i] <= n:
        if bk[a[i]] == 0:
            heapq.heappush(del_que, a[i])
        bk[a[i]] += 1
    print(del_que)
    while len(del_que) and del_que[0] == que[0]:
        heapq.heappop(que)
        heapq.heappop(del_que)
        print(que)
        print(del_que)
    print(que[0])
