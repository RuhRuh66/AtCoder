N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

if X < A[0] or X > A[N-1]:
    print('No')
    exit()
    
low = 0
high = N-1

while (high - low) >= 0:
    m = (high + low)//2
    if A[m] == X:
        print('Yes')
        exit()
    
    elif X > A[m]:
        low = m+1
    else:
        high = m-1


print('No')
    
    
