N, M = map(int, input().split())

X = list(map(int, input().split()))

X = sorted(X)
Y = []
for i in range(M-1):
    temp = X[i+1] - X[i]
    Y.append(temp)
    
Y = sorted(Y, reverse = True)

ans = sum(Y[N-1:])

print(ans)