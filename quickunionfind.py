class QuickUnionFind(object):
    def __init__(self, n):
        self.id = [i for i in range(0, n)]
        self.size = [1] * n

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
        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] = self.size[j] + self.size[i]
        else:
            self.id[j] = i
            self.size[i] = self.size[i] + self.size[j]

    def count(self):
        number_of_nodes = 0
        nodes = set()
        for i in range(len(self.id)):
            node_to_check = self.root(i)
            if not node_to_check in nodes:
                nodes.add(node_to_check)
                number_of_nodes = number_of_nodes + 1

        return number_of_nodes        