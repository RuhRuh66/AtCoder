N = int(input())
A = list(map(int, input().split()))

ans = 0

for i in range(N):
    A_min = 10**10
    for j in range(i, N):
        A_min = min(A_min, A[j])
        ans = max(ans, A_min * (j-i+1))
        
print(ans)