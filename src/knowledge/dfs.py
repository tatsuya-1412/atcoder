N = 4  # node数
G = [[1], [2, 3], [1], [1]]  # 隣接node

used = [False] * N
start = 0


# 再帰
def dfs(v):
    used[v] = True
    for w in G[v]:
        if not used[w]:
            dfs(w)


dfs(start)


# スタック
s = [start]
while len(s) > 0:
    v = s.pop()
    if not used[v]:
        used[v] = True
        for w in G[v]:
            if not used[w]:
                s.append(w)
