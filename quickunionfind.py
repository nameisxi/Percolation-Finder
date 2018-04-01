class QuickUnionFind(object):
    def __init__(self, n):
        self.id = [i for i in range(0, n)]
        self.size = [1] * n

    def find_root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.find_root(p) == self.find_root(q)

    def union(self, p, q):
        i = self.find_root(p)
        j = self.find_root(q)
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
            node_to_check = self.find_root(i)
            if not node_to_check in nodes:
                nodes.add(node_to_check)
                number_of_nodes = number_of_nodes + 1

        return number_of_nodes        