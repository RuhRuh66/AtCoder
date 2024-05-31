X = input()

c = [0, len(X)]

for i in range(len(X)-1):
    if X[i] == 'T' and X[i+1] == 'S':
        c.append(i+1)
        
c.sort()

ans = 0
for j in range(len(c)-1):
    part = X[c[j]:c[j+1]]
    ans += abs(part.count('T') - part.count('S'))
    
print(ans)

