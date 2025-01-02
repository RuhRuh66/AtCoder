def merge_sort(A:list):
    m = len(A)
    if m <= 1:
        return A
    
    n = m//2
    
    left = merge_sort(A[:n])
    right = merge_sort(A[n:])
    
    return merge(left, right)

def merge(left, right):
    p, q = 0, 0
    seq = []
    while (p < len(left) and q<len(right)):
        if left[p] >= right[q]:
            seq.append(right[q])
            q += 1
        else:
            seq.append(left[p])
            p += 1
            
    seq += left[p:]
    seq += right[q:]
    
    return seq   
    
    

N = int(input())
A = list(map(int, input().split()))

print(*merge_sort(A)) 