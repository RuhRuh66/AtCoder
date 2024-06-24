S = input()

l  =len(S)

i = 0
ans = 0
conseq_A = 0

while i < l-1:
    if S[i] == 'A':
        conseq_A += 1
        i += 1
        
    elif S[i] == 'B' and S[i+1] == 'C':
        ans += conseq_A
        i += 2
        
    else:
        conseq_A = 0
        i += 1
        
print(ans)
        
        
    




