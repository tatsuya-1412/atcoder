class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # 要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # 要素xが属するグループと要素yが属するグループとを併合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 要素xが属するグループのサイズ（要素数）を返す
    def size(self, x):
        return -self.parents[self.find(x)]

    # 要素x, yが同じグループに属するかどうかを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)


# https://note.nkmk.me/python-union-find/
