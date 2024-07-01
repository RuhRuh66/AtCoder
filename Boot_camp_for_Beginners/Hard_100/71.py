N = int(input())
A = list(map(int, input().split()))

B = [A[i]- (i+1) for i in range(N)]

B.sort()

ans = 0
if N % 2 == 1:
    m = N//2
    for i in range(N):
        ans += abs(B[i]-B[m])
else:
    m = N//2
    med = (B[m-1] + B[m])//2
    for i in range(N):
        ans += abs(B[i]-med)

print(ans)   