S = input()

max_len = 0

count = 0
for i in range(len(S)):
    if S[i] in ['A', 'C', 'G', 'T']:
        count += 1
    else:
        max_len = max(max_len, count)
        count = 0
        
print(max_len)