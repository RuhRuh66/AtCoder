class UnionFind():
    def __init__(self, n) :
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

    def size(self, x):
        return -self.parents[self.find(x)]
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

N, M = map(int, input().split())

uf = UnionFind(N)

x = 0
for _ in range(M):
    a, b, c, d = input().split()
    if uf.same(int(a)-1, int(c)-1):
        x += 1
    uf.union(int(a)-1, int(c)-1)


y = 0
for i in range(N):
    if uf.parents[i] < 0:
        y += 1
        
print(x, y-x)
