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
        
    def unite(self, x, y):
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

for i in range(K):
    a, b = map(int, input().split())
    B[a-1].append(b-1)
    B[b-1].append(a-1)



friends = UnionFind(N)        

for i in range(N):
    for k in A[i]:
        friends.unite(i, k)
    

C=[]
for i in range(N):
    cnt = 0
    for k in B[i]:
        if friends.same(i, k):
            cnt += 1
    ans = friends.size(i) - len(A[i]) -cnt -1
    C.append(ans)
    
print(*C)
    
    