N, K = map(int, input().split())
A = list(map(int, input().split()))


R=0
sum = 0
ans = 0


for l in range(N):
    while sum < K:
        if R == N:
            break
        sum += A[R]
        R += 1
    if sum >= K:
        ans += N-R+1
        sum -= A[l]
        

print(ans)
        

        

