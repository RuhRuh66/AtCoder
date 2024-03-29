N = int(input())
L = list(map(int, input().split()))

import sys
import bisect

sys.setrecursionlimit(10**6)
INF = 10**18

L.sort()

rlt = 0

for i in range(N):
    for j in range(i+1, N):
        a = L[i]
        b = L[j]
        
        r = bisect.bisect_left(L, a+b)
        temp = r-j-1
        
        rlt += temp
        
print(rlt)
