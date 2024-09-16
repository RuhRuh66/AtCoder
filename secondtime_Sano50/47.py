
def op(x, y):
    return min(x, y)

inf = 10**10


class SegTree():
    def __init__(self, N, array, e, op):
        self.N = N
        self.e = e
        M = self.N.bit_length()
        self.op = op
        self.bu = 2**M
        self.tree = [self.op] * (2**M)
        
        
        