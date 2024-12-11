N = int(input())

A = set()

for i in range(1, int((N+1)**0.5)+1):
    if N % i == 0:
        A.add(i)
        A.add(N//i)
        
print(*A)
    
    