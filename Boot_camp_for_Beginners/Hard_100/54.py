X, Y, A, B, C = map(int, input().split())

P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

P.sort(reverse=True)
Q.sort(reverse=True)
R.sort(reverse=True)

S = P[:X] + Q[:Y]
ans = sum(S)
S.sort()

for i in range(min(C, X+Y)):
    if S[i] < R[i]:
        ans += R[i] -S[i]
    else:
        break
print(ans)