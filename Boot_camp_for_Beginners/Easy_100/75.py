N, K = map(int, input().split())
A = []
for i in range(N):
    A.append(int(input()))
    
A = sorted(A)

ans = 1000000000
for i in range(N-K+1):
    ans = min(ans, A[i+K-1]-A[i])

print(ans)