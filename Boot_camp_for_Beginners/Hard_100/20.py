N, M = map(int, input().split())

import bisect

A = [[] for i in range(N)]
B = []

for i in range(M):
    p, y = map(int, input().split())
    A[p-1].append(y)
    B.append((p, y))

A_sorted = [sorted(i) for i in A]

for j in range(M):
    p, y = B[j]
    state_code = p
    city_code = bisect.bisect_left(A_sorted[p-1], y)
    
    print(str(state_code).zfill(6)+str(city_code+1).zfill(6))