N, K = map(int, input().split())
A = [0]+list(map(int, input().split()))

from itertools import accumulate
B = list(accumulate(A))

if B[N] < K:
    print(0)
    exit()
    
 
ans = 0
for i in range(1, N+1):
    if A[i] >= K:
        ans += N-i+1
    else:
        s = B[N]-B[i-1]
        if s< K:
            break
        else:
            ng = i
            ok = N
            while ok - ng > 1:
                mid = (ok+ng)//2
                if (B[mid]-B[i-1]) >= K:
                    ok = mid
                else:
                    ng = mid
            ans += N+1-ok
            
print(ans)
                
        
        


