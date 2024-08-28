N = int(input())
S = list(str(input()))
Q = int(input())


    
cond = 1

for j in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        if cond == 1:
            S[a-1], S[b-1] = S[b-1], S[a-1]
        else:
            if a <= N:
                if b <=N:
                    S[a-1+N], S[b-1+N] = S[b-1+N], S[a-1+N]
                else:
                    S[a-1+N], S[b-1-N] = S[b-1-N], S[a-1+N]
            else:
                if b <=N:
                    S[a-1-N], S[b-1+N] = S[b-1+N], S[a-1-N]
                else:
                    S[a-1-N], S[b-1-N] = S[b-1-N], S[a-1-N]
    if t == 2:
        cond = 1 - cond
        

if cond == 1:
    print(''.join(S))
else:
    print(''.join(S[N:2*N]) + ''.join(S[:N]))