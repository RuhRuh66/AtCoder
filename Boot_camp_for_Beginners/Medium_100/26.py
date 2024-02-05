N = int(input())

A = list(map(int, input().split()))
B= []
for i in range(N-1):
    if A[i+1] > A[i]:
        B.append('LT')
    elif A[i+1] == A[i]:
        B.append('E')
    else:
        B.append('GT')
        
