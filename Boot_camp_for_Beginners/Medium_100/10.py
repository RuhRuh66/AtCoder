N = int(input())
A = [0] * 100010

for i in map(int, input().split()):
    A[i] += 1
    A[i-1] += 1
    A[i+1] += 1
    
print(max(A))
