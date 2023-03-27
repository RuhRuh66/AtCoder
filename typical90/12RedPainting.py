class UnionFind():
    def __init__(self, n) :
        self.n = n
        self.parents = [-1] * (n+1)

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
    

H, W = map(int, input().split())
import sys
sys.setrecursionlimit(10**6)

uf = UnionFind(H*W)
adj = [[-1, 0], [1, 0], [0, -1], [0, 1]]

color_red = [[False]*W for i in range(H)]

Q = int(input())
for k in range(Q):
    i = list(map(int, input().split()))
    if len(i) == 3:
        if color_red[i[1]-1][i[2]-1] == False:
            color_red[i[1]-1][i[2]-1] = True
            x = uf.find((i[1]-1)*W+(i[2]-1))
            for j in adj:
                r = (i[1]-1) + j[0]
                c = (i[2]-1) + j[1]
                if 0 <= r < H and 0 <= c < W:
                    if color_red[r][c] == True:
                        uf.union((i[1]-1)*W+(i[2]-1), r*W+c)
              
    if len(i) == 5:
        if color_red[i[1]-1][i[2]-1] == True and color_red[i[3]-1][i[4]-1] == True and (uf.find((i[1]-1)*W+(i[2]-1)) == uf.find((i[3]-1)*W+(i[4]-1))):
            print('Yes')
        else:
            print('No')
            

            
                
            
    



