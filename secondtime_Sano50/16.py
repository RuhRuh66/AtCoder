N, K = map(int,input().split())
T = [list(map(int, input().split())) for _ in range(N)]

from itertools import permutations

cities = [i for i in range(1, N)]

count = 0
for v in permutations(cities, N-1):
    total = 0
    for j in range(N-2):
        total += T[v[j]][v[j+1]]
    total += T[0][v[0]]    
    total += T[v[N-2]][0]
    if total == K:
        count += 1

print(count)
    






    