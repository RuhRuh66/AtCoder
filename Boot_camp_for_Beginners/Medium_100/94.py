A, B, X = map(int, input().split())
from math import log10

ok = 0
ng = X+1

while ng-ok >1:
    mid = (ok+ng)//2
    if A*mid + B*int(log10(mid)+1) <= X:
        ok = mid
    else:
        ng = mid

if ok >= 10**9:
    print(10**9)
else:
    print(ok)