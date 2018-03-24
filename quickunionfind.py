class QuickUnionFind(object):
    def __init__(self, n):
        self.id = []
        self.sz = []
        for i in range(n):
            self.id[i] = i;
            self.sz[i] = 1

    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] = self.sz[j] + self.sz[i]
        else:
            id[j] = i
            self.sz[i] = self.sz[i] + self.sz[j]