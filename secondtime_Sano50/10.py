N = int(input())

i = 1
A = []
while i*i < N:
    if N % i == 0:
        A.append(i)
        A.append(N//i)
        
    i += 1
    
if i * i == N:
    A.append(i)

A.sort()

print(*A)