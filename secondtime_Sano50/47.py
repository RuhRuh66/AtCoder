def op(x, y):
    return x ^ y

from math import ceil, log2
class SegTree():
    def __init__(self, N, array, e, op):
        self.N = N
        self.array = array
        self.e = e
        self.op = op
        self.m = ceil(log2(N))
        self.tree = [self.e] * (2**(self.m+1))
        for i in range(N):
            self.tree[i+(2**self.m)] = self.array[i]
        for j in range(2**self.m-1, 0, -1):
            self.tree[j] = self.op(self.tree[2*j], self.tree[2*j+1])
            
    def update(self, x, y):
        n = x + (2**self.m)
        self.tree[n] = self.op(self.tree[n], y)
        while n > 1:
            if n % 2 == 0:
                self.tree[n//2] = self.op(self.tree[n], self.tree[n+1])
            
            else:
                self.tree[n//2] = self.op(self.tree[n], self.tree[n-1])
                
            n //= 2
            
    def query(self, x, y):
        l = x + (2**self.m)
        r = y + (2**self.m) +1
        
        result = self.e
        while l<r:
            if l % 2 == 1:
                result = self.op(result, self.tree[l])
                l += 1
                
            if r % 2 == 1:
                result = self.op(result, self.tree[r-1])
                
            l //= 2
            r //= 2
            
        return result
                
                
N, Q = map(int, input().split())
A = list(map(int, input().split()))

s = SegTree(N, A, 0, op)

for i in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        s.update(x-1, y)

    else:

        print(s.query(x-1, y-1))
        
