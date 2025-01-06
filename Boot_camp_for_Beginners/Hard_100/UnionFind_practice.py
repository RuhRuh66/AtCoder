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

    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def size(self, x):
        return -self.parents[self.find(x)]
    

N, M, K = map(int, input().split())
A = [[] for _ in range(N)]
B = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    A[a-1].append(b-1)
    A[b-1].append(a-1)

for j in range(K):
    a, b = map(int, input().split())
    B[a-1].append(b-1)
    B[b-1].append(a-1)


taro = UnionFind(N)

for i in range(N):
    for a in A[i]:
        taro.union(i, a)

for i in range(N):
    n = taro.size(i)
    direct = len(A[i])
    dislike = 0
    for j in B[i]:
        if taro.same(i, j):
            dislike += 1
    print(n-direct-dislike-1)
