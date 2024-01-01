N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

earn = 0
for i in range(N):
    if B[N-1-i] >= A[N-i]:
        earn += A[N-i]
        B[N-1-i] -= A[N-i]
        if B[N-1-i] >= A[N-i-1]:
            earn += A[N-i-1]
            A[N-i-1] = 0
        else:
            earn += B[N-1-i]
            A[N-1-i] -= B[N-1-i]
    else:
        earn += B[N-1-i]
print(earn)