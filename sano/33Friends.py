N,M = map(int, input().split())
mem = []
for i in range(M):
    temp = list(map(int, input().split()))
    mem.append(temp)
    

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        