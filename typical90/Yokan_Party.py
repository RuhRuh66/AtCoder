N, L = map(int, input().split())
K = int(input())
A = [0]+list(map(int, input().split())) + [L]



def check(l):
    left_index = 0
    right_index = 0
    cnt = 0
    
    while right_index < len(A):
        if (A[right_index] - A[left_index]) < l:
            right_index += 1
        else:
            cnt += 1
            left_index = right_index
            right_index += 1
            
    if cnt >= K+1:
        return True
    else:
        return False
    
ok = -1
ng = L
while ng-ok>1:   
    mid = (ok+ng)//2
    if check(mid) == True:
        ok = mid
    else:
        ng = mid
        
print(ok)
    
    