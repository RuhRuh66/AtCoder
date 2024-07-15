N, K = map(int, input().split())

from math import floor

q = floor((N-K)/(K+1))


ans = 0

for k in range(K, N):
    ans += N-k

    if q < 1:
        print(ans)
        exit()
    else:    
        for i in range(1, q+1):
            for j in range(k+1, N+1):
                if i * j + k <= N:
                    ans += 1
                
print(ans)
    