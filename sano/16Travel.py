N, K = map(int, input().split())
T = []
for i in range(N):
    temp = list(map(int, input().split()))
    T.append(temp)

from itertools import permutations
A = [i for i in range(1, N)]
roots = permutations(A)

count = 0
for i in roots:
    i = [0] + list(i) + [0]
    time = 0
    for k in range(N):
        time += T[i[k]][i[k+1]]
    if time == K:
        count += 1
        
print(count)        
        
    