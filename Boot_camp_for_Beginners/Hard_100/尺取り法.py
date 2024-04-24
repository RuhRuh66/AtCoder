N, K = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
ans = 0
r = 0

for l in range(N):
    while sum < K:
        if r == N:
            break
        else:
            sum += A[r]
            r += 1
    
    if sum < K:
        break
     
    ans += N-r+1      
    sum -= A[l]
    
print(ans)
    