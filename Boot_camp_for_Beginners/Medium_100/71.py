N = int(input())

A = list(map(int, input().split()))

total = sum(A)
Su = 0
ara = total - Su

ans = 10**20
for i in range(N-1):
    Su += A[i]
    ara -= A[i]
    ans = min(ans, abs(Su-ara))
    
print(ans)
