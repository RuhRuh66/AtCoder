N, M, C = map(int, input().split())

B = list(map(int, input().split()))

A = []
for i in range(N):
    temp = list(map(int, input().split()))
    A.append(temp)

ans = 0
for j in range(N):
    sums = C
    for k in range(M):
        sums += A[j][k] * B[k] 
    if sums > 0:
        ans += 1
        
print(ans)
    