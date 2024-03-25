S = input()

count = 0

for i in range(len(S)-1):
    if S[i+1] == S[i]:
        continue
    else:
        count += 1
        
        
print(count)
        
        