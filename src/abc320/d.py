from collections import defaultdict


def dfs(v, x, y):
    visited[v] = True
    pos[v] = (x, y)
    for vv, dx, dy in G[v]:
        if not visited[vv]:
            dfs(vv, x + dx, y + dy)


n, m = map(int, input().split())
G = defaultdict(list)

for i in range(m):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, x, y))
    G[b].append((a, -x, -y))

pos = [None] * n
visited = [False] * n

dfs(0, 0, 0)

for i in range(n):
    if visited[i]:
        print(pos[i][0], pos[i][1])
    else:
        print("undecidable")
