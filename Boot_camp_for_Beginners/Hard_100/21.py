n = int(input())
A = list(map(int,input().split()))

A.sort()

import bisect
from math import comb

mid = A[n-1] /2

ans = []
l = bisect.bisect_left(A, mid)
if l == 0:
    ans = [A[n-1], A[0]]
    
elif l == n-1:
    ans = [A[n-1], A[n-2]]
    
else:
    if abs(A[l] - mid) < abs(A[l-1] - mid):
        ans = [A[n-1], A[l]]
    else:
        ans = [A[n-1], A[l-1]]
        
print(*ans)

