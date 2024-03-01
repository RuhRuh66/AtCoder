N, M = map(int, input().split())

ans = 0
if M - 2*N >= 0:
    ans = N + (M - 2*N)//4
else:
    ans = M//2
    
    
print(ans)