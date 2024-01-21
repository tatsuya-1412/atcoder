from collections import deque

N = 4  # node数
G = [[1], [2, 3], [1], [1]]  # 隣接node

used = [False] * N
start = 0

# キュー
q = deque([start])
while len(q) > 0:
    v = q.popleft()
    if not used[v]:
        used[v] = True
        for w in G[v]:
            if not used[w]:
                q.append(w)
