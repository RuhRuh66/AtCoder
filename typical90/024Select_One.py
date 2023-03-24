N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

balance = 0
for i in range(N):
    balance += abs(A[i]-B[i])
    if balance > K:
        print('No')
        exit()
        
        
        

if abs(balance - K) % 2 == 0:
    print('Yes')
else:
    print('No')