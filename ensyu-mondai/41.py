T = int(input())
N = int(input())

dif = [0] * (T+1)

for i in range(N):
    L, R = map(int, input().split())
    dif[L] += 1
    dif[R] -= 1
    
n  = 0    
for i in range(T):
    n += dif[i]
    print(n)
   