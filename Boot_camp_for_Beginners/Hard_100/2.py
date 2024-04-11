N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 10**9 + 7

cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            cnt += 1
        else:
            continue

add = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            add += 1
 
 
inc = (K-1)*K//2 % mod           
ans = (cnt * K + add * inc) % mod

print(ans)
            