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
        
    
N, M = map(int, input().split())


edges = []
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b))

ans = 0
for i in range(M):
    uf = UnionFind(N)
    for j in range(M):
        if i != j:
            a, b = edges[j]
            uf.union(a, b)
    temp = 0
    for n in uf.parents:
        if n < 0:
            temp += 1
    if temp >= 2:
        ans += 1
        
print(ans)
    
    
    
        
        