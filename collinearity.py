N = int(input())
A = []
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

status = False
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if (A[j][0] - A[i][0]) * (A[k][1] - A[i][1]) == (A[k][0] - A[i][0]) * (A[j][1] - A[i][1]):
                status = True
                break

if status == True:
    print('Yes')
else:
    print('No')