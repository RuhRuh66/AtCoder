N, X = map(int, input().split())

L = [0] * (N+1)
P = [0] * (N+1)
L[0] = 1
P[0] = 1

for i in range(1,N+1):
    L[i] = L[i-1] * 2 + 3
    P[i] = P[i-1] * 2 + 1
    
def patty_count(N, X):
    if  N == 0:
        return 0 if X == 0 else 1
    else:
        if X == 1:
            return 0
        elif 1 < X < L[N-1] + 2:
            return patty_count(N-1, X-1)
        elif X == L[N-1] + 2:
            return P[N-1] +1
        elif X > L[N-1] + 2:
            return patty_count(N-1, X-L[N-1]-2) + P[N-1] + 1

print(patty_count(N, X))