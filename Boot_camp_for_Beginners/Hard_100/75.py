N, K = map(int, input().split())

S = input()



pre = 0
for i in range(N-1):
    if S[i+1] == S[i]:
        pre += 1
        

n_N = N-pre


ans = pre + min(n_N-1, 2*K)
    
print(ans)
        