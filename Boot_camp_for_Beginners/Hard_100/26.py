K, T = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

if A[0]-1 < K-A[0]:
    print(0)
    exit()
else:
    print(2*A[0]-1-K)

    
