n, m = map(int, input().split())
d = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    d[a][b] = c
    d[b][a] = c

ans = 0
seen = [False for _ in range(n+1)]

def dfs(v, l):
    global ans
    seen[v] = True
    if l > ans: ans = l
    for i in range(1, n+1):
        if not seen[i] and d[v][i]:
            dfs(i, l + d[v][i])
    seen[v] = False

for i in range(1, n+1):
    dfs(i, 0)

print(ans)
