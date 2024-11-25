N = int(input())
S = str(input())

ans = 0

for i in range(1000):
    s = str(i)
    if len(s)==1:
        s = '00' + s
    if len(s) == 2:
        s = '0' + s
    
    if (x := S.find(s[0])) != -1:
        if (y := S.find(s[1], x+1)) != -1:
            if(z := S.find(s[2], y+1)) != -1:
                ans += 1
                
print(ans)
    
    


        
    