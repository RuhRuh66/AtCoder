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
        
        
uf = UnionFind(N)
for i in range(M):
    x =mem[i][0]-1
    y = mem[i][1]-1
    uf.union(x, y)
    
print(-min(uf.parents))
    
        