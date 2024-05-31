K = int(input())

a = [*range(1, 10)]
if K <= 9:
    print(K)
    exit()
    
import sys
sys.setrecursionlimit(10**8)

def rec(d, val, all:list):
    all.append(val)
    if d == 10:
        return
    
    for j in range(-1, 2):
        add = val % 10 + j
        if 0 <= add <= 9:
            rec(d+1, val*10+add, all)
            
all = []
for v in range(1, 10):
    rec(1, v, all)

all.sort()

print(all[K-1])
            
            
        
    