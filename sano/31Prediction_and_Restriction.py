N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())


def judge(A):
    B = ['a'] * len(A)
    B[0] = 'kachi'
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            B[i] = 'kachi'
        else:
            if B[i-1] == 'kachi':
                B[i] = 'make'
            else:
                B[i] = 'kachi'
                
    return B   

def haitou(A, B):
    ans = 0
    for i in range(len(A)):
        if B[i] == 'kachi':
            if A[i] == 'r':
                ans += P
            elif A[i] == 's':
                ans += R
            else:
                ans += S
    return ans


total = 0
for i in range(K):
    T_i = T[i:N:K]
    B_i = judge(T_i)
    total += haitou(T_i, B_i)
    
print(total)