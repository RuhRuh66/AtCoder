N, M, X, Y = map(int, input().split())
routes = [[] for i in range(N+1)]
for i in range(M):
    A, B,T, K = map(int, input().split())
    routes[A].append([B, T, K])
    routes[B].append([A, T, K])


from heapq import heappop, heappush
from math import ceil


from heapq import heappop, heappush
from math import ceil

confirmed =[False] * (N+1)
time = [10**20] * (N+1)

time[X] = 0
que = []
heappush(que, [0, X])


while len(que) > 0:
    now_time, now_place = heappop(que)
    if confirmed[now_place] == True:
        continue
    confirmed[now_place] = True
    for to_place, T, K in routes[now_place]:
        if confirmed[to_place] == False:
            to_time = ceil(now_time/K) * K + T
            if to_time < time[to_place]:
                time[to_place] = to_time
                heappush(que, [to_time, to_place])
            
if time[Y] == 10**20:
    print(-1)
else:
    print(time[Y])







    
    
    



    





