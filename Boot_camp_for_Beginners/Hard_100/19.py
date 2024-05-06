H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

B = dict()
for i in range(1, N+1):
    B[i] = A[i-1]
    
B = list(sorted(B.items(), key= lambda x:x[1], reverse=True))

C = []

for i in range(N):
    n, m = B[i]
    temp = [n]*m
    C += temp
    

ans = []
for i in range(H):
    temp2 = C[i*W:(i+1)*W]
    if i %2 == 0:
        print(*temp2)
    else:
        print(*reversed(temp2))
    
