from math import log10
N = int(input())

st = int(N**0.5)

status = True
while status:
    if N % st == 0:
        ans = int(log10(N//st)) + 1
        print(ans)
        exit()
        
    else:
        st -= 1
    

    
        