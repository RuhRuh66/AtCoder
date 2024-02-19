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

print(B)
        
for j in range(N-2):
    if B[j+1] == 'E' or B[j+1] == B[j]:
        continue
    else:
        B[j+1] = 'Sep'

print(B)
print(B.count('Sep') +1)
