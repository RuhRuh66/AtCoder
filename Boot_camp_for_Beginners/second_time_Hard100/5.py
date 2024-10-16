N, M = map(int, input().split())
A = list(map(int, input().split()))

B = [-i for i in A]

from heapq import heapify, heappop, heappush

heapify(B)

for i in range(M):
    c = heappop(B)
    d = -(-c//2)
    heappush(B, d)
    
print(-sum(B))