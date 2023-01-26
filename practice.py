def segfunc(x, y):
    return x+y

class SegTree():
    def __init__(self, x_list, init, segfunc):
        self.x_list = x_list
        self.init = init
        self.segfunc = segfunc
        self.height = len(x_list).bit_length() + 1
        self.tree = [init] * (2**self.height)
        self.num = 2 ** (self.height-1)
        for i in range(len(x_list)):
            self.tree[2**(self.height-1) + i] = x_list[i]
        for i in range(self.num-1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])
            
if __name__ == '__main__':
    a = [5, 7, 8]
    n = SegTree(a, 0, segfunc)
    print(n.height)
    print(n.num)
    print(n.tree)
    print(n.x_list)
    print(n.tree[n.num:])
    
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        