N = int(input())
S = input()

ans = 0

for i in range(1, N):
    a = S[0:i]
    b = S[i:N]
    A = set(a)
    B = set(b)
    
    ans = max(ans, len(A.intersection(B)))
    
print(ans)
