N, M = map(int, input().split())
friends = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    friends[a-1].append(b-1)
    friends[b-1].append(a-1)
    
    
class UnionFind():
    def __init__(self, n):
        self.parents=[-1] * n
        self.n = n
        
    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        
    def size(self):
        return min(self.parents)
    
    
k = UnionFind(N)

for j in range(N):
    temp = friends[j]
    for l in temp:
        k.unite(j, l)

print(-k.size())
    
        