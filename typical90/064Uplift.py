N, Q = map(int, input().split())
A = list(map(int, input().split()))

B = []
for i in range(N-1):
    dif = A[i+1] -A[i]
    B.append(dif)

    
ans = sum(abs(b) for b in B)

for _ in range(Q):
    L, R, V = map(int, input().split())
    L = L-1
    R = R-1
    
    if L == 0:
        if R == N-1:
            ans = ans
        else:
            before = abs(B[R])
            B[R] -= V
            after = abs(B[R])
            ans += after-before
    else:
        if R == N-1:
            before = abs(B[L-1])
            B[L-1] += V
            after = abs(B[L-1])
            ans += after - before
        else:
            before = abs(B[L-1]) + abs(B[R])
            B[L-1] += V
            B[R] -= V
            after = abs(B[L-1]) + abs(B[R])
            ans += after - before
    print(ans)
       
        
    
        

        
       