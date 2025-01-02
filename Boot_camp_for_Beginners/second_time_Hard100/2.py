N, K = map(int, input().split())
A = list(map(int, input().split()))

count_1 = 0
count_2 = 0

for i in range(N-1):
    for j in range(i, N):
        if A[i] > A[j]:
            count_1 += 1
            
for k in range(N):
    for l in range(N):
        if A[k] > A[l]:
            count_2 += 1
            
mod = 10**9+7

ans = (count_1 * K + (K*(K-1)//2) * count_2) % mod

print(ans)