H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

B = []

for i in range(N):
    for j in range(A[i]):
        B.append(i+1)
        
C = [[0] * W for _ in range(H)]

for k in range(H*W):
    l = k // W
    c = k % W
    
    C[l][c] = B[k]
    

for n in range(H):
    if n % 2 == 0:
        print(*C[n])
        
    else:
        print(*C[n][::-1])