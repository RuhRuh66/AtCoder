S = input()
N = len(S)

l = 0
r = N-1

count = 0
while r>l:
    if S[l] == S[r]:
        l += 1
        r -= 1
    elif S[l] == 'x' and S[r] != 'x':
        l += 1
        count += 1
    elif S[l] != 'x' and S[r] == 'x':
        r -= 1
        count += 1
    else:
        print(-1)
        exit()
        
print(count)





    
    
