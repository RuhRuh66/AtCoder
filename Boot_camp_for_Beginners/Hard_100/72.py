N = int(input())

for m in range(1, 3500):
    for h in range(1, 3500):
        d = 4*m*h-m*N-h*N
        t = N*m*h
        if d < 1:
            continue
        if t % d != 0:
            continue
        w = t//d
        
        print(m, h, w)
        exit()
                
          
         
                
