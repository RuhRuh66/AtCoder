N, M = map(int, input().split())
A = list(map(int, input().split()))
minus_A = []
for i in A:
    minus_A.append(-1*i)
    
import heapq
heapq.heapify(minus_A)
import math

for j in range(M):
    s = heapq.heappop(minus_A)
    t = math.ceil(s/2)
    heapq.heappush(minus_A, t)
    
print(-sum(minus_A))
    
