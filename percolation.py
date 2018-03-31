from quickunionfind import QuickUnionFind


class Percolation(object):
    def __init__(self, width):
        #
        self.width = width
        self.number_of_sites = width**2
        self.number_of_open_sites = 0
        # Site state initalization
        self.sites_states = [False] * (self.number_of_sites + 2)
        self.sites_states[0] = True
        self.sites_states[self.number_of_sites + 1] = True
        # Union Find object initalization
        self.union_find = QuickUnionFind(width + 2)
        self.union_find_adjustor = QuickUnionFind(width + 1)


    def is_open(self, i, j):
        if i < 1 or i > self.width or j < 1 or j > self.width:
            raise IndexError
        site_to_open = (i - 1) * self.width + j
        return self.sites_states[site_to_open]


    def open_site(self, i, j):
        if i <=0 or j <= 0 or i > self.width or j > self.width:
            raise IndexError

        if self.is_open(i, j):
            return     

        site_to_open = (i - 1) * self.width + j
        self.sites_states[site_to_open] = 1
        self.number_of_open_sites = self.number_of_open_sites + 1

        if j != 1 and self.is_open(i, j - 1):
            self.union_find.union(site_to_open - 1, site_to_open)
            self.union_find_adjustor.union(site_to_open - 1, site_to_open)
        
        if j != self.width and self.is_open(i, j + 1):
            self.union_find.union(site_to_open + 1, site_to_open)
            self.union_find_adjustor.union(site_to_open + 1, site_to_open)
        
        if i != 1 and self.is_open(i - 1, j):
            self.union_find.union(site_to_open - self.width, site_to_open)
            self.union_find_adjustor.union(site_to_open - self.width, site_to_open)
        
        if i != self.width and self.is_open(i + 1, j):
            self.union_find.union(site_to_open + self.width, site_to_open)
            self.union_find_adjustor.union(site_to_open + self.width, site_to_open)
        
        if site_to_open <= self.width:
            self.union_find.union(0, site_to_open)
            self.union_find_adjustor.union(0, site_to_open)
        
        if site_to_open > self.number_of_sites - self.width:
            self.union_find.union(self.number_of_sites + 1, site_to_open)
        


    def is_full(self, i, j):
        if i < 1 or j > self.width or j < 1 or j > self.width:
            raise IndexError

        site_to_open = (i - 1) * self.width + j
        return self.union_find.connected(0, site_to_open) and self.union_find_adjustor.connected(0, site_to_open)


    def get_number_of_open_site(self):
        return self.number_of_open_sites    


    def percolates(self):
        return self.union_find.connected(0, self.number_of_sites + 1)               
