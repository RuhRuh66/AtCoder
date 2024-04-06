from collections import defaultdict

N, K = map(int, input().split())

T = defaultdict(int)

for i in range(N):
    a, b = map(int, input().split())
    T[a] += b


L = list(sorted(T.items()))


cnt = 0
for x, y in L:
    cnt += y
    if cnt >= K:
        print(x)
        exit()
        

    
