N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

from bisect import bisect_left

ans = 0

for i in range(N):
    j = bisect_left(B, A[i]+1)
    gt = N-j
    if j+1 < N:
        k = bisect_left(C, B[j+1])
        gt2 = N-k
        ans += gt*gt2
    
print(ans)
