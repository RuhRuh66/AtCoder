N = int(input())
A = list(map(int, input().split()))

mod = 10**9+7

if A[0] != 0:
    print(0)
    exit()
    
    
now = [1, 0, 0]

ans = 3
for i in range(1, N):
    if now.count(A[i]) == 0:
        print(0)
        exit()
    else:
        ans = (ans * now.count(A[i])) % mod
        s = now.index(A[i])
        now[s] += 1
    
print(ans % mod)
