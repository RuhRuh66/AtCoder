s = input()
t = input()

s = sorted(list(s))
t = sorted(list(t), reverse = True)

len_s = len(s)
len_t = len(t)

if len_s<len(t):
    for i in range(len_s):
        if s[i] < t[i]:
            print('Yes')
            exit()
            
        elif s[i] == t[i]:
            continue
        
        else:
            print('No')
            exit()
    print('Yes')
 
if len_s==len(t):
    for i in range(len_s):
        if s[i] < t[i]:
            print('Yes')
            exit()
            
        elif s[i] == t[i]:
            continue
        
        else:
            print('No')
            exit()
    print('No')
    
if len_s>len(t):
    for i in range(len_t):
        if s[i] < t[i]:
            print('Yes')
            exit()
            
        elif s[i] == t[i]:
            continue
        
        else:
            print('No')
            exit()
    print('No')
    
    

    
    
   
    
