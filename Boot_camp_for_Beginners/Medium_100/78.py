S = input()
K = int(input())

seq_nu = []
c = 1
for i in range(len(S)-1):
    if S[i+1] == S[i]:
        c += 1
        
    else:
        seq_nu.append(c)
        c = 1
        
seq_nu.append(c)  
if S[0] != S[-1]:
    ans = 0
    for j in seq_nu:
        if j >= 2:
            ans += j // 2
    ans *= K
else:
    L = len(seq_nu)
    if L == 1:
        ans = (seq_nu[0] * K) //2
        
    else:
        head = seq_nu[0] // 2
        tail = seq_nu[L-1]//2
        mid1 = 0
        mid2 = 0
        for k in range(1, L-1):
            mid1 += seq_nu[k]//2
        mid2 += (seq_nu[0]+seq_nu[L-1])//2
            
        ans = head + mid1 * K + mid2*(K-1) + tail
        
        
print(ans)

       
            
    
        