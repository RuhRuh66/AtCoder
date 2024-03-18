N, M = map(int, input().split())
S = input()
T = input()


from math import lcm, gcd

L = lcm(N, M)
G = gcd(N, M)

common_chr = []
for i in range(G):
    temp = (L//G) * i
    common_chr.append(temp)
    
a = [i//(M//G) for i in common_chr]
b = [j//(N//G) for j in common_chr]

for k in range(G):
    if S[a[k]] != T[b[k]]:
        print(-1)
        exit()
print(L)


    





