N, K = map(int, input().split())

A = list(map(str, input().split()))
B = {str(i) for i in range(10)}


for j in range(K):
    B.remove(A[j])
    
B = set(B)
    
flag = False


while flag == False:
    check = set(str(N))
    if check <= B:
        flag = True
    else:
        N += 1
    

print(N)
        
     
        
        
        