
A = {}
for i in range(26):
    A[chr(i+97)] = 26-i
 
A[0] = 0

s = str(input())
K = int(input())
s_ans = list(s)



for j in range(len(s)):
    if s[j]  == 'a':
        continue
    else:
        if A[s[j]] <= K:
            s_ans[j] = 'a'
            K -= A[s[j]]
        else:
            continue

if K > 0:
    s_ans[-1] = chr(ord(s_ans[-1]) + (K%26))
              
print(''.join(s_ans))
    




   