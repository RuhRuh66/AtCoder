N  = int(input())
desitinations = [[] for i in range(N+1)]
for i in range(1, N):
    A, B = map(int, input().split())
    desitinations[A].append(B)
    desitinations[B].append(A)
    


        



                
        
            
    