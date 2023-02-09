N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

x = 0
for i in range(N):
    x += A[i]*B[i]

if x == 0:
    print('Yes')
else:
    print('No')