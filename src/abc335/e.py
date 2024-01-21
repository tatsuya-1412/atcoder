import sys

input = sys.stdin.readline


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)


n, m = map(int, input().split())
a = list(map(int, input().split()))
uf = UnionFind(n)
vp = [[] for _ in range(max(a) + 1)]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if a[u] > a[v]:
        u, v = v, u
    if a[u] == a[v]:
        uf.union(u, v)
    else:
        vp[a[u]].append((u, v))

dp = [-(10**9)] * n
dp[uf.find(0)] = 1

for nx in vp:
    for u, v in nx:
        u = uf.find(u)
        v = uf.find(v)
        if dp[u] > 0:
            dp[v] = max(dp[v], dp[u] + 1)

ans = max(0, dp[uf.find(n - 1)])
print(ans)
