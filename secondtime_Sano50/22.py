N, K = map(int, input().split())
P = list(map(int, input().split()))

ex_v = []

for i in range(N):
    ex =(1+P[i])*P[i]/(2*P[i])
    ex_v.append(ex)
    
    
ans = 0
temp = 0
for i in range(K):
    temp += ex_v[i]

for j in range(N-K+1):
    temp = max(temp-ex_v[j]+ex_v[K+j], temp)


print(temp)