N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0

for i in range(N):
    if A[i] > B[i]:
        cnt -= A[i]-B[i] 
    elif A[i] < B[i]:
        cnt += (B[i]-A[i])//2
        
if cnt >= 0:
    print('Yes')
else:
    print('No')



