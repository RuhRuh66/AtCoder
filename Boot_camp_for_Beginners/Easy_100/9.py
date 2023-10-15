N = int(input())
K = int(input())
X = list(map(int, input().split()))

ans = 0

for i in range(N):
    temp = min(abs(X[i]), abs(X[i]-K))
    ans += 2 * temp


print(ans)