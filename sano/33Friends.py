from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
        
    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        