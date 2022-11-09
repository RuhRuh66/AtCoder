N, X = map(int, input().split())
A = []
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

total_alc = 0
count = 1
for i in range(N):
    total_alc += A[i][0] * A[i][1]
    if total_alc > X * 100:
        break
    else:
        count += 1

if total_alc <= 100 * X:
    print(-1)
else:
    print(count)