S = input()

#R

ans = [0]*len(S)

count = 0
for i in range(len(S)):
    if S[i] == 'R':
        count += 1
    else:
        if count % 2 == 1:
            ans[i-1] += count//2 + 1
            ans [i] += count//2
        else:
            ans[i-1] += count//2
            ans[i] += count//2
            
        count =0
count = 0
for j in range(len(S)-1, -1, -1):
    if S[j] == 'L':
            count += 1
    else:
        if count % 2 == 1:
            ans[j+1] += count//2 + 1
            ans [j] += count//2
        else:
            ans[j+1] += count//2
            ans[j] += count//2
            
        count =0



print(*ans)
            


