K = int(input())

mods = set()
mods.add(7)

if K == 1 or K == 7:
    print(1)
    exit()

A = [0] * (K+1)
A[1] = 7
for i in range(2, K+1):
    A[i] = (A[i-1] * 10 + 7) % K
    if A[i] == 0:
        print(i)
        exit()

print(-1)

    

        
        