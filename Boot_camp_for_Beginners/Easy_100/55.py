N, D = map(int, input().split())

X = []
for i in range(N):
    temp = list(map(int, input().split()))
    X.append(temp)
    
from itertools import combinations

count = 0
for i, j in combinations(range(N), 2):
    dist = 0
    for d in range(D):
        dist += ((X[i][d]-X[j][d]))**2
    k = dist**0.5
    if k.is_integer():
        count += 1
        

print(count)
    