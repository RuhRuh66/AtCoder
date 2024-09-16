H, N = map(int, input().split())

DP = [10**10] * (H+1)
DP[0] = 0

for i in range(N):
    A, B = map(int, input().split())
    for j in range(H+1):
        if j + A<= H:
            DP[j+A] = min(DP[j+A], DP[j]+B)
            
        else:
            DP[H] = min(DP[j]+B, DP[H])
            
print(DP[H])