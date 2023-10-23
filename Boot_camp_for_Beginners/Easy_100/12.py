K, N = map(int, input().split())
A = list(map(int, input().split()))

dist = []
for i in range(N-1):
    temp = A[i+1] - A[i]
    dist.append(temp)
    
last_dist = A[0] + K-A[N-1]

dist.sort(reverse=True)

ans = K-max(dist[0], last_dist)
print(ans)