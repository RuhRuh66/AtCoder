N = int(input())
A = list(map(int, input().split()))

L = 0
R = sum(A)
dif = 10**12

for i in range(N):
    L += A[i]
    R -= A[i]
    dif = min(dif, abs(L-R))
    
print(dif)
    
    