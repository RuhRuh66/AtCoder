N = int(input())
S = input()
A = [0]+[0 if s == '.' else 1 for s in S]

from itertools import accumulate

s = sum(A)
A_acc = list(accumulate(A))

if s == 0 or s == N:
    print(0)
    exit()

ans = 10**6
for i in range(N+1):
    l = A_acc[i]
    r = N-i-(s-A_acc[i])
    dif = l+r
    ans = min(ans, dif)
print(ans)

      
            

