N = int(input())

A = list(map(int, input().split()))

odds = 1
for i in range(N):
    if A[i] % 2 == 0:
        odds *= 2
    else:
        odds *= 1
        
print(3**N - odds)