N = int(input())
A = list(map(int, input().split()))

x = 0
for i in range(N):
    if i % 2 == 0:
        x += A[i]
    else:
        x -= A[i]
        
result = [0] * N

result[0] = x

for j in range(1, N):
    result[j] = 2*A[j-1] - result[j-1]

print(*result)
    