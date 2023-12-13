S = input()
S = list(S)

count = 0
t = ''
prev = ''
for i in range(len(S)):
    t += S[i]
    if prev != t:
        count += 1
        prev = t
        t = ''
    else:
        continue
print(count)
    
        
      
        
    
    