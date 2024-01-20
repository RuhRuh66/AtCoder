S = input()
N = len(S)

T = [-1] * (N+1)
lt = 0
gt = 0

for i in range(N):
    if S[i] == '<':
        if lt == 0:
            T[i] = 0
        T[i+1] = T[i] + 1
        lt += 1
    else:
        lt = 0

for j in reversed(range(1, N+1)):
    if S[j-1] == '>':
        if gt == 0:
            T[j] = 0
        T[j-1] = max(T[j-1], T[j] + 1)
        gt += 1
    else:
        gt = 0
        
print(sum(T))


