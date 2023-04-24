N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]

def check_length(l):
    left_idx = 0
    for i in range(K+1):
        right_idx = left_idx
        while right_idx < len(A) and (A[right_idx] - A[left_idx]) < l:
            right_idx += 1
            if right_idx == len(A):
                return False
        left_idx = right_idx
    return True

ok = 0
ng = L + 1

while ng - ok > 1:
    mid = (ok+ng)//2
    
    if check_length(mid):
        ok = mid
    else:
        ng = mid
print(ok)
        
    
    








    
        
        
    

     
        
         