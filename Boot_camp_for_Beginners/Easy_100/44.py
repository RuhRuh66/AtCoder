S = list(input())

s = [int(i) for i in S]

count = 0
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        s[i] = (s[i]+1) % 2
        count += 1
        
print(count)
        
        
        
    

