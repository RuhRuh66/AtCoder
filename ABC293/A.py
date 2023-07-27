s = list(input())


for i in range(1, len(s)//2 + 1):
    s[2*i-2], s[2*i-1] = s[2*i-1], s[2*i-2]


    
ans = ''
for j in s:
    ans+=j
print(ans)