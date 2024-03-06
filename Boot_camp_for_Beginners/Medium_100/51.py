N = int(input())

X = list(map(int, input().split()))

import copy

Y = copy.deepcopy(X)
Y.sort()

K = Y[N//2-1]

for i in range(N):
    if X[i] <= K:
        ans = Y[N//2]
    else:
        ans = Y[N//2-1]

    print(ans)
