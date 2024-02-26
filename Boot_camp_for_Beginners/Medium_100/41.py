s = input()



def check_all(liter):
    k = set(liter)
    if len(k) == 1:
        return True
    else:
        return False
    
if check_all(s):
    print(0)
    exit()

ans = 10**6
for i in range(26):
    c = chr(97+i)
    S = s
    flag = False
    count = 0    
    
    while flag == False:
        count += 1
        T=''
        for i in range(len(S)-1):
            if S[i] == c or S[i+1] == c:
                T += c
            else:
                T += S[i]
        flag = check_all(T)
        S = T
    ans = min(ans, count)
        

print(ans) 
            
            
    
    