N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [-i for i in A]

from heapq import heapify, heappop, heappush

heapify(B)

while M >0:
    temp = int(heappop(B)/2)
    heappush(B, temp)
    M -= 1
    
print(-sum(B))

