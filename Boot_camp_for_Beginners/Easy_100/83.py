N = int(input())
A = []
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A.append(A1)
A.append(A2)


sums = sum(A2)

start = A[0][0] + sums
ans = start


for i in range(1, N):
    now = start-A[1][i-1]+ A[0][i]
    ans = max(ans, now)
    start = now

print(ans)