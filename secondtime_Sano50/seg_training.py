def op(x,y):
    return min(x,y)

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
            self.tree[i+2**self.m] = self.array[i]

        for j in range(2**self.m-1, 0, -1):
            self.tree[j] = self.op(self.tree[2*j], self.tree[2*j+1])

    def update(self, x, y):
        n = x + 2**self.m
        self.tree[n] = y
        while n > 1:
            if n % 2 == 0:
                self.tree[n//2] = self.op(self.tree[n], self.tree[n+1])
            else:
                self.tree[n//2] = self.op(self.tree[n-1], self.tree[n])
            n //= 2


e = 10**10
N = 7
array = [2, 6, 10, 8, 4, 3, 9]

s = SegTree(N, array, e, op)

s.update(1,5)
print(s.tree)