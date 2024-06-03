N = int(input())

A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))
inf = 10 ** 9

order = [1]

DP = [inf] * (N+1)
DP[1] = 0
DP[2] = A[1]
for i in range(3, N+1):
    if DP[i-2]+B[i-1] <= DP[i-1]+A[i-1]:
        order.append(i-2)
    else:
        order.append(i-1)
    DP[i] = min(DP[i-2]+B[i-1], DP[i-1]+A[i-1])

print(order)