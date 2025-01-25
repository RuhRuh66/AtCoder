N = int(input())
A = [0] + list(map(int, input().split()))



ac = [0] * (N+1)
for i in range(1, N+1):
    ac[i] += (ac[i-1]+A[i-1])

ans = 0

M = int(input())
B1 = int(input())

pre = B1
for i in range(2, M+1):
    nex = int(input())
    ans += abs(ac[nex]-ac[pre])
    pre = nex
    
print(ans)