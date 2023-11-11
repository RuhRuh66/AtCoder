N, M = map(int, input().split())

L = 1
R = N


for i in range(M):
    A, B = map(int, input().split())
    L = max(L, A)
    R = min(R, B)
    
if R>=L:
    ans = R-L+1
else:
    ans = 0
    
print(ans)
    