A, B, X = map(int, input().split())

from math import log10

def cost(n):
    keta = len(str(n))
    return A*n + B*keta

if X >= cost(10**9):
    print(10**9)
    exit()
if X < cost(1):
    print(0)
    exit()

ok = 1
ng = 10**20
while ng-ok > 1:
    mid = (ok+ng)//2
    if cost(mid) <= X:
        ok = mid
    else:
        ng = mid

print(ok)
    
    




