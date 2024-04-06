N, M = map(int, input().split())

mod = 10**9+7
A = set() 
for i in range(M):
    temp = int(input())
    A.add(temp)
    
DP = [-1] * (N+1)
DP[0] = 1

if 1 not in A:
    DP[1] = 1
    for i in range(2, N+1):
        if i not in A:
            if DP[i-1] != -1:
                if DP[i-2] != -1:
                    DP[i] = (DP[i-1] + DP[i-2]) % mod
                else:
                    DP[i] = DP[i-1] % mod
            else:
                if DP[i-2] != -1:
                    DP[i] = DP[i-2] % mod

                else:
                    print(0)
                    exit()
else:
    DP[1] = -1
    for i in range(2, N+1):
        if i not in A:
            if DP[i-1] != -1:
                if DP[i-2] != -1:
                    DP[i] = DP[i-1] + DP[i-2] % mod

                else:
                    DP[i] = DP[i-1] % mod

            else:
                if DP[i-2] != -1:
                    DP[i] = DP[i-2] % mod

                else:
                    print(0)
                    exit()
   
print(DP[N] % mod)