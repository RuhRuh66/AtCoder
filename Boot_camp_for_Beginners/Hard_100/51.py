X, Y = map(int, input().split())

mod = 10**9 + 7

if (X+Y) % 3 != 0:
    print(0)
    exit()
    

    
else:
    K = (X+Y)//3
    n = (2*X-Y) // 3
    m = (2*Y-X) // 3
    
    if n < 0 or m < 0:
        print(0)
        exit()
    elif n == 0 or m == 0:
        print(1)
        exit()
        
    else:
        c = n if n <= m else m
        
        numerator = 1
        for i in range(K-c+1, K+1):
            numerator = numerator * i % mod
        
        denominator = 1
        for j in range(1 ,c+1):
            denominator = denominator * j % mod
          
            

        ans = numerator * pow(denominator, -1, mod) % mod
            
        

        print(ans)
        
  
