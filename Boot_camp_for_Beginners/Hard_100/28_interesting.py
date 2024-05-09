N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = 10**9
for i in range(N-K+1):
    l = i
    r = i+K-1
    
    A = abs(X[l]) + abs(X[r]-X[l])
    B = abs(X[r]) + abs(X[r]-X[l])
    temp = min(A, B)
    
    ans = min(ans, temp)
    
print(ans)