N = int(input())

if N < 6:
    print(N)
    exit()
    

A = []
i = 6
while i <100000:
    A.append(i)
    i *= 6
    
j = 9
while j < 100000:
    A.append(j)
    j *= 9
    
A.sort()

# print(A)

DP = [0] * (N+1)

for i in range(1, 6):
    DP[i] = i

for j in range(6, N+1):
    DP[j] = min(DP[j-1]+1, min([DP[j-k]+1 for k in A if j-k >= 0]))
            

print(DP[N])


