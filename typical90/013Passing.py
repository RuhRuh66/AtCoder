
from heapq import heappush, heappop
N, M = map(int, input().split())

roads= [[] for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    roads[A-1].append([B-1, C])
    roads[B-1].append([A-1, C])
    
def diks(a):
    confirmed = [False] * N
    dist = [float('inf')] * N
    
    start = a
    dist[start] = 0
    
    
    q = [(dist[start], start)]
    
    while q:
        distance, now = heappop(q)
        confirmed[now] = True
        
        for next_city, weight in roads[now]:
            if confirmed[next_city] == True:
               continue
            if dist[next_city] < distance + weight:
                continue
            dist[next_city] = distance + weight
            heappush(q, (dist[next_city], next_city))
            
    return dist

from_first = diks(0)
from_last = diks(N-1)

for i in range(N):
    ans = from_first[i] + from_last[i]
    print(ans)
    
    