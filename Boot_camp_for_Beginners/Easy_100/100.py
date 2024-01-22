N = int(input())
A = [0] + list(map(int, input().split()))

count = 0

for i in range(1, N+1):
    if A[A[i]] == i:
        count += 1
        
print(count//2)
        