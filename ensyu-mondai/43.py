class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * self.n
        
    def find(self, x):
       if self.parent[x] < 0:
           return x
       else:
           self.parent[x] = self.find(self.parent[x])
           return self.parent[x]
        
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        
        if self.parent[x] > self.parent[y]:
            x, y = y, x
            
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        
a = 'The graph is connected.'
b = 'The graph is not connected.'


N, M = map(int, input().split())

t = UnionFind(N)
for i in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    t.unite(x, y)


if len(list(filter(lambda x: x<0, t.parent))) ==1:
    print(a)
else:
    print(b)
    
            
        
        
        
